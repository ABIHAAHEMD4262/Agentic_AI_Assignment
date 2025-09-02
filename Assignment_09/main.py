
from dynamic_instructions.instructions import hotel_instructions,HotelContext,hotels_data
import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner
from typing import  Optional

load_dotenv()

# Step 4: Define the agent
agent = Agent(
    name="Hotel Assistant",
    instructions=hotel_instructions,
)


# Step 5: Auto-detect hotel from user query
def detect_hotel_from_query(user_message: str) -> Optional[str]:
    msg = user_message.lower()
    if "pearl" in msg:
        return "pearl"
    elif "crown" in msg:
        return "crown"
    elif "hotel one" in msg or "one" in msg:
        return "one"
    return None


# Step 6: Run assistant
async def main():
    user_queries = [
        "Tell me about Hotel Pearl",
        "What facilities does Hotel Crown offer?",
        "How much does Hotel One cost per night?",
        "Do you have info about hotels?"
    ]

    for query in user_queries:
        hotel_choice = detect_hotel_from_query(query)
        context = HotelContext(hotel=hotel_choice)

        print(f"\nUser: {query}")
        result = await Runner.run(agent, query, context=context)
        print(f"Assistant: {result.final_output}")


if __name__ == "__main__":
    asyncio.run(main())