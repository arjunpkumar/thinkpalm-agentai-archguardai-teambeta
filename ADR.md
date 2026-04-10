# Architecture Decision Record (ADR): Agentic Arch Reviewer

## 1. Context and Problem Statement
Manual architectural reviews are time-intensive and subjective. We require an automated system that can navigate a GitHub repository independently, identify design patterns, and provide actionable scalability recommendations. The system must be resilient to LLM provider volatility and maintain high functional integrity.

## 2. Design Decisions

### 2.1 Orchestration Framework: LangGraph (v1.0+)
* **Decision:** Utilize `langgraph.prebuilt.create_react_agent` for the agentic loop.
* **Rationale:** Traditional linear chains are insufficient for repository analysis. LangGraph implements a state-machine based **ReAct (Reasoning and Acting)** loop, allowing the agent to "think," call a tool, observe the result, and "think" again.
* **Trade-off:** Higher complexity in state management, but offers significantly higher reliability for multi-step code exploration.

### 2.2 LLM Strategy: Multi-Model Resilience via OpenRouter
* **Decision:** Implement a dynamic model selector in the UI.
* **Rationale:** Development revealed frequent `429 RateLimit` and `404 ToolSupport` errors on free-tier providers.
* **Key Choice:** Validated `openai/gpt-oss-120b:free` as the primary stable model for tool-use tasks.

### 2.3 Sensory Tools (Capabilities)
The agent is decoupled from the GitHub API via two specific tools:
1.  **`list_repo_files`**: Maps the repository structure (limited to 100 files).
2.  **`read_specific_file`**: Fetches raw content (capped at 5,000 characters).

---

## 3. Implementation & Validation

### 3.1 Data Flow
1.  **Mapping:** Agent invokes `list_repo_files` to understand the project landscape.
2.  **Exploration:** Agent identifies entry points (e.g., `main.dart`, `pubspec.yaml`) and selectively invokes `read_specific_file`.
3.  **Synthesis:** Agent analyzes code chunks and generates a structured report.

### 3.2 GitHub API Optimization
* **Decision:** Authenticated Header-based Requests.
* **Rationale:** Increases the API rate limit from 60 to 5,000 requests/hr via `GITHUB_TOKEN`.

### 3.3 Validation Strategy (Testing)
* **Decision:** Implementation of an Integration Testing suite using `pytest`.
* **Rationale:** Testing agentic systems is difficult due to non-deterministic LLM outputs. Our strategy focuses on **Functional Contracts**:
    * **Tool Validation:** Ensuring GitHub utilities return valid strings and handle 404s.
    * **Graph Integrity:** Verifying that the LangGraph agent compiles and reaches a terminal state.
    * **Connectivity:** Confirming OpenRouter and GitHub API handshake stability.

---

## 4. Evaluation of Trade-offs
* **Agentic Latency vs. Accuracy:** The loop is slower than a single prompt but prevents "hallucinated architecture" by forcing the agent to fetch real file data before speaking.
* **Integration Tests vs. Mocks:** We opted for real integration tests in this prototype to verify network reliability, acknowledging that a production CI/CD pipeline would eventually require mocked responses to conserve API credits.

## 5. Future Evolution
* **Visual Graph Output:** Integration of Mermaid.js for visual diagrams.
* **Human-in-the-loop:** Adding breakpoints in LangGraph for human approval of expensive token-heavy file reads.