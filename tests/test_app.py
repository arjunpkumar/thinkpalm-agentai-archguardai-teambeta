import pytest
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from app import fetch_repo_structure, read_github_file

# Load env for API keys
load_dotenv()

@pytest.fixture
def test_repo():
    return "https://github.com/arjunpkumar/flutter_base"

@pytest.fixture
def llm():
    return ChatOpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
        model="openai/gpt-oss-120b:free",
        temperature=0
    )

def test_github_fetch_structure(test_repo):
    """Test if we can fetch the file tree from a Flutter repo."""
    structure = fetch_repo_structure(test_repo)
    assert structure is not None
    # CHANGE: Look for Flutter-specific files instead of main.py
    assert "pubspec.yaml" in structure.lower() or "lib/main_dev.dart" in structure.lower()
    assert "Error" not in structure

def test_github_read_file(test_repo):
    """Test if we can read the README of the Flutter repo."""
    content = read_github_file(test_repo, "README.md")
    assert content is not None
    assert "flutter" in content.lower()
    assert len(content) > 0

def test_agent_initialization(llm):
    """Test if the LangGraph agent compiles correctly with tools."""
    from langchain_core.tools import Tool

    tools = [
        Tool(name="test_tool", func=lambda x: "done", description="test")
    ]
    agent = create_react_agent(llm, tools)

    # Check if it's a compiled graph
    assert hasattr(agent, "invoke")

def test_agent_full_loop(llm, test_repo):
    """Integration Test: Check if the agent can perform a simple reasoning task."""
    from langchain_core.tools import Tool

    tools = [
        Tool(name="list_files", func=lambda x: fetch_repo_structure(test_repo), description="list")
    ]
    agent = create_react_agent(llm, tools)

    inputs = {"messages": [("user", "What is the top level directory structure?")]}
    result = agent.invoke(inputs)

    assert len(result["messages"]) > 1
    assert isinstance(result["messages"][-1].content, str)