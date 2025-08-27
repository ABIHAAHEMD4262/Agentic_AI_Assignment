from agents import Agent,  Runner,function_tool
from dotenv import load_dotenv

load_dotenv()

@function_tool
def get_weather(city:str) -> str:
    """Returns mock weather info for the given city."""
    return f"The current temperature in any {city} is 34℃ with clear skies."

def main():
    print("Welcome to the Weather Info Agent!")
    print("Ask me about the weather in any city. Type 'exit' tp quit.\n")

    agent = Agent(
        name = "Weather Bot",
        instructions="You are a weather assistant. Use the weaher tool to provide informatin when needed.",
        tools= [get_weather]
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