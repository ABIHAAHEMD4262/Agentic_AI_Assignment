# Assignment 06 – Customer Support Bot


## 📌 Project Overview
This project demonstrates how to build a **multi-agent system** using the `openai-agents` SDK.  
It includes two agents:  
- **HumanAgent** – takes input from the user.  
- **BotAgent** – responds to user queries using AI.  

The project also implements a **Guardrail** to block abusive or negative inputs. If the user tries to send abusive language, the bot will not process it and instead show a warning message.

---

## 🚀 Features
- ✅ Human-agent to bot-agent interaction.  
- ✅ Guardrail to **filter abusive or negative inputs**.  
- ✅ Friendly and safe conversation flow.  
- ✅ Modular code using **dataclasses** and **Pydantic BaseModel**.  

---

📂 Project Structure
```bash
Assignment_06/
│── main.py               # Main entry point
│── my_agents/
│    └── agents.py        # HumanAgent and BotAgent
│── my_guardrails/
│    └── guardrail.py     # Guardrail for abusive input
│── requirements.txt      # Dependencies
│── README.md             # Project documentation

---

💡 Example Conversation
```bash
🤖 Support Bot (Agents SDK) — type 'exit' to quit

You: What's your working hour?
Bot: Our customer support hours are typically from 9:00 AM to 6:00 PM, Monday through Friday. If you need assistance outside 
these hours, feel free to leave us a message and we'll get back to you as soon as possible!
You: What the status of order id 1003?
Bot: It looks like I couldn't find any order with the ID "1003." Please check the order number—it should look something like 
ORD-1001. If you have the correct ID, just send it over and I’ll check again!
You: Check again my order id is 1003?
Bot: It looks like the order ID "1003" isn't recognized. Please double-check your order number—it should look something like 
"ORD-1003." Let me know the correct ID, and I'll be happy to check it for you!
You: yes, this my order id ORD-1003  
Bot: Your order ORD-1003 has been delivered. If you need help with your order or have any other questions, please let me know!
You: You are fool
Bot: ⚠️ I cannot respond to abusive or unsafe language.
You: quit
👋 Goodbye!
