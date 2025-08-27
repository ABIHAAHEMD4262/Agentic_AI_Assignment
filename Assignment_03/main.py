import os
from agents import Agent, Runner,function_tool
from dotenv import load_dotenv


load_dotenv()
@function_tool
def Substract(a:int , b:int):
     """Substract two numbers"""
     print("Substract tool fired ---->")
     return a - b
  


@function_tool
def Add(a:int , b:int):
    """Add two numbers"""
    print("Add tool fired ---->")
    return a+b

@function_tool
def Divide(a:int , b:int):
    """Divide two numbers"""
    print("Divide tool fired ---->")
    return a / b

@function_tool
def Multiply(a:int , b:int):
    """Multiply two numbers"""
    print("Multiply tool fired ---->")
    return a * b


def main():
    print("🤖 Welcome to the Math Tool Agent!")
    print("Type 'exit' to end the converstion.\n")


    agent = Agent(
        name = "Math Agent",
        instructions="You are a helpful math agent. Use the add tool when needed.",
        tools= [Add, Substract, Multiply, Divide]
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

       
