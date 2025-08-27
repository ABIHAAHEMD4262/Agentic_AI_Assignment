import os
from agents import Agent, OpenAIChatCompletionsModel, Runner,AsyncOpenAI ,set_tracing_disabled
from dotenv import load_dotenv
from agents.run import RunConfig

load_dotenv()
set_tracing_disabled(True)
gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_PATH")
gemini_model_name = os.getenv("GEMINI_MODEL_NAME")


if not gemini_api_key:
    raise ValueError("GEMINI API KEY not found in .env!")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url=gemini_base_url
)

model = OpenAIChatCompletionsModel(
    openai_client=external_client,
    model=gemini_model_name
)

config = RunConfig(model=model)

def main():
    print("🤖 Welcome to the FAQ Bot")
    print("Type 'exit' to end the converstion.\n")


    agent = Agent(
        name = "FAQ Bot",
        instructions="You are a helpful FAQ bot.",
        model=model
    )

    while True:
        user_question = input("❓ You: ")
        if user_question.lower() in ["exit", "quit"]:
           print("👋 Goodbye!")
           break

        result =  Runner.run_sync(agent, user_question)
        print("🤖 Bot: ", result.final_output)

if __name__ == "__main__":
    main()

       
