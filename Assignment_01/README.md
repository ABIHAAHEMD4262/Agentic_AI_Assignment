🧑‍💻 Assignment 01 – Simple Agent with OpenAI SDK & Chainlit
📌 Objective

The goal of this project is to:

1. Build a simple AI agent using Python and the OpenAI Agents SDK.

2. Create an interactive web interface for the agent using Chainlit.

3. Connect the Chainlit interface with the agent so the bot can leverage LLM capabilities for dynamic conversations.
   

🚀 Features

🧠 AI agent powered by OpenAI Agents SDK

💬 Interactive chat interface with Chainlit

📜 Maintains chat history per user session

⚡ Real-time response generation


💻 How It Works

When a user starts chatting, a chat history is stored per session.

Each message is passed along with previous history to the agent.

The agent processes the request via Runner.run_sync(math_agent, context_prompt).

The AI response is appended to history and displayed in the Chainlit UI.


🔄 Flow Diagram
flowchart TD

    A[👤 User Message] --> B[💬 Chainlit UI]
    B --> C[📜 Store Chat History]
    C --> D[🧠 Runner.run_sync(math_agent, context_prompt)]
    D --> E[⚡ Agent Generates Response]
    E --> F[📜 Save Response in History]
    F --> G[💬 Display Response in Chainlit UI]

