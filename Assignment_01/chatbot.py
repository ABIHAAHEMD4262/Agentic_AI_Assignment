import chainlit as cl
from run_level import  math_agent
from agents import Runner

# 🔁 Store per-user history
@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("chat_history", [])

@cl.on_message
async def main(message: cl.Message):
    prompt = message.content
    history = cl.user_session.get("chat_history")

    # Append the current user message to history
    history.append({"role": "user", "content": prompt})

    await cl.Message(content="Bhai jan sochne do...").send()

    # Combine history into a conversation string
    context_prompt = "\n".join([f"{m['role']}: {m['content']}" for m in history])

    # Call the agent with the full history
    result = Runner.run_sync(
        math_agent,
        context_prompt
    )

    # Save AI reply to history
    history.append({"role": "assistant", "content": result.final_output})

    # Update session memory
    cl.user_session.set("chat_history", history)

    # Send response to frontend
    await cl.Message(content=f"{result.final_output}").send()
