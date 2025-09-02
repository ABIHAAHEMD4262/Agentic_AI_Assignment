🏨 Hotel Assistant (Assignment 9)

📌 Objective

Convert static instructions into dynamic ones using OpenAI’s Agent SDK.

This project extends the original bilal_fareed_code hotel assistant so that:

A single agent can store and retrieve details for multiple hotels.

The agent auto-detects the hotel from the user’s query.

If no hotel is mentioned, the agent asks the user to specify a hotel.


⚙️ Features

✅ Supports multiple hotels (Hotel Pearl, Hotel Crown, Hotel One)
✅ Dynamic instructions — agent responds differently based on context
✅ Auto-detection of hotel name from the user query


🔍 How It Works

-Hotel Data is stored in a dictionary (hotels_data).

-HotelContext keeps track of which hotel is being asked about.

-Dynamic Instructions are generated based on the hotel context.

-Hotel Detection is done by scanning the user’s query.

-The agent responds only with details of the detected hotel.



📖 Learning Outcome

-This assignment demonstrates how to:

-Replace static instructions with dynamic instructions.

-Use context to modify an agent’s behavior.

-Build a multi-entity assistant using OpenAI’s Agent SDK.🔍 How I-t Works

-Hotel Data is stored in a dictionary (hotels_data).

-HotelContext keeps track of which hotel is being asked about.

-Dynamic Instructions are generated based on the hotel context.

-Hotel Detection is done by scanning the user’s query.

-The agent responds only with details of the detected hotel.


Example Output

```bash
User: Tell me about Hotel Pearl
Assistant: Hotel Pearl is located in Karachi with 120 rooms. Facilities include Free WiFi, Pool, Gym, and Spa. Price range: PKR 10,000 - 25,000 per night.

User: What facilities does Hotel Crown offer?
Assistant: Hotel Crown provides WiFi, a Conference Hall, and Airport Pickup.

User: How much does Hotel One cost per night?
Assistant: Hotel One in Islamabad costs PKR 6,000 - 15,000 per night.

User: Do you have info about hotels?
Assistant: Please specify which hotel (Pearl, Crown, or One).






