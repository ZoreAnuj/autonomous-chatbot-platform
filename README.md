# Autonomous Chatbot Platform

This project is an experimental platform for building and managing next-generation autonomous AI chatbots. It explores architectures for creating persistent, self-improving conversational agents that can handle complex, multi-turn tasks.

## Key Features
*   Autonomous agent core with goal-oriented task execution
*   Long-term memory and context management for persistent conversations
*   Modular plugin system for extending chatbot capabilities
*   Basic web interface for interaction and agent monitoring

## Tech Stack
*   **Backend:** Python, FastAPI
*   **AI/ML:** LangChain, OpenAI API
*   **Memory:** Vector Database (Chroma/FAISS)
*   **Frontend:** Next.js, React

## Getting Started
1.  Clone the repo: `git clone https://github.com/zoreanuj/autonomous-chatbot-platform.git`
2.  Install dependencies: `pip install -r requirements.txt`
3.  Set your `OPENAI_API_KEY` environment variable.
4.  Run the development server: `uvicorn main:app --reload`