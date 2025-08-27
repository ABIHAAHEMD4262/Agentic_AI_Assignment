Assignment 05 – Agent with Multiple Tools
🎯 Objective

Build an AI agent that can use multiple tools. Specifically:

Perform math operations (addition).

Answer weather queries with a mock weather function.

Choose the correct tool automatically depending on user input.


📝 Tasks

Define two tools:

add(a, b) → returns the sum of two numbers.

get_weather(city) → returns mock weather info for a city.

Register both tools with the agent.

Let the agent decide which tool to use when the user asks a question.

Test with both math and weather queries.


Example interaction:

  Welcome to the Weather Info Agent and Math Agent!
Ask me about the weather in any city and addition questions. Type 'exit' or 'quit'.

❓ You: What is the weather of Karachi?
🤖 Bot: The current temperature in any Karachi is 34 ℃ with clear skies.

❓ You: What is 5 + 7?
🤖 Bot: 12
