# 🏗️ Agentic Arch Reviewer
**"Beyond static analysis: An AI Agent that thinks like a Tech Lead."**

## 📝 Project Name & Problem Statement
**Project Name:** Agentic Architecture Reviewer (AAR)

**Problem Statement:**
Manual architectural reviews are time-consuming and prone to human oversight. Traditional static analysis tools (linters) find syntax bugs but cannot identify high-level design patterns (like Clean Architecture or BLoC) or suggest structural improvements. This project provides an autonomous AI Agent that navigates a codebase like a human engineer—reading file structures and selectively analyzing code to provide high-level architectural insights.

---

## 👥 Team Members and Their Contributions
* **[Your Name]**:
    * **Agent Orchestration:** Designed the LangGraph state machine to replace legacy linear chains.
    * **Tool Engineering:** Built the authenticated GitHub ingestion tools for recursive mapping and file content extraction.
    * **Resilience Logic:** Implemented the OpenRouter provider-switching logic to handle 429 Rate Limits and 404 Tool Support errors.
    * **Frontend:** Developed the Streamlit dashboard for interactive repository analysis.

---

## 💻 Tech Stack with Versions
| Technology | Version | Purpose |
| :--- | :--- | :--- |
| **Python** | 3.10+ | Core Runtime |
| **Streamlit** | 1.32.0 | Frontend UI & Dashboard |
| **LangGraph** | 0.0.30 | Agent State-Machine Orchestration |
| **LangChain OpenAI** | 0.1.0 | LLM Integration Layer |
| **Python-Dotenv** | 1.0.1 | Secure Secret Management |
| **OpenRouter API** | 2026 Stable | Multi-model Gateway |
| **GitHub API** | v3 | Data Ingestion |

---

## 🚀 Step-by-Step: How to Run Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/arjunpkumar/flutter_base.git](https://github.com/arjunpkumar/flutter_base.git)
cd thinkpalm-agentai-archguardai-teambeta
```
## Set Up a Virtual Environment
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate

3. Install Required Packages
   pip install streamlit langchain-openai langgraph requests python-dotenv

4. Create your .env File
   OPENROUTER_API_KEY=your_key_here
   GITHUB_TOKEN=your_personal_access_token_here

5. Start the App
   streamlit run app.py

📸 Screenshots of Working Prototype
!   [Main Dashboard](screenshots/1.png)
!   [Main Dashboard](screenshots/2.png)
!   [Main Dashboard](screenshots/3.png)
!   [Main Dashboard](screenshots/4.png)
!   [Main Dashboard](screenshots/5.png)
!   [Main Dashboard](screenshots/6.png)
!   [Main Dashboard](screenshots/7.png)
!   [Main Dashboard](screenshots/8.png)
!   [Main Dashboard](screenshots/9.png)

🎥 5-min Demo Link
Demo Highlights:

Handling Rate Limits: Demonstrating switching to gpt-oss-120b when other models are saturated.

Autonomous Navigation: The agent deciding which files to read based on the file tree.

Final Report: Reviewing the AI-generated architecture suggestions for a Flutter project.