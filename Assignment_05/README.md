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
```
❓ You: What is the weather of Karachi and what is 2 + 2? 
Weather function fired---->
Add Function Called ----->
🤖 Bot:  The current weather in Karachi is 34°C with clear skies. Also, 2 + 2 equals 4.
❓ You: exit
👋 Goodbye!



