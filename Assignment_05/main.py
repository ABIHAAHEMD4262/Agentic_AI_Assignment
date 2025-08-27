
from agents import Agent, Runner ,ModelSettings
from dotenv import load_dotenv
from my_tools.tools import get_weather, add

load_dotenv()

def main():
    print("Welcome to the Weather Info Agent and Math Agent!")
    print("Ask me about the weather in any city and addition questions. Type 'exit' or 'quit'.\n")

    agent = Agent(
        name = "Assistant",
        instructions="You are helpful assistant.",
        tools= [get_weather,add],
        model_settings=ModelSettings(tool_choice="required")
    )

    while True:
        user_question = input("❓ You: ")
        if user_question.lower() in ["exit", "quit"]:
           print("👋 Goodbye!")
           break

        result =  Runner.run_sync(agent, user_question  )
        print("🤖 Bot: ", result.final_output)

if __name__ == "__main__":
    main()