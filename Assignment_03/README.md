➕ Assignment – Math Tool Agent
📌 Objective

The goal of this project is to build an agent that can use math functions as tools to answer user questions.
For example, when asked “What is 5 + 7?”, the agent automatically calls the Add function.

📝 Tasks Completed

✅ Defined Python functions for addition, subtraction, multiplication, and division.

✅ Registered these functions as tools with the agent using @function_tool.

✅ Built an agent that can decide when to use the correct tool.

✅ Tested the agent with at least three math questions.


🔄 Flow Diagram
flowchart TD

    A[👤 User Question] --> B[🤖 Math Agent]
    B --> C{Which Tool Needed?}
    C -->|Addition| D[➕ Add Function]
    C -->|Subtraction| E[➖ Subtract Function]
    C -->|Multiplication| F[✖ Multiply Function]
    C -->|Division| G[➗ Divide Function]
    D --> H[💬 Return Answer]
    E --> H
    F --> H
    G --> H
    H --> I[✅ Show Response to User]
    
🔄 Interaction

<img width="311" height="285" alt="Assignment_03" src="https://github.com/user-attachments/assets/e8cbf838-1e09-4239-b758-c0bd37af2c45" />
