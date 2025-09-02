from data.data import hotels_data
from typing import Literal, Optional
from agents import RunContextWrapper, Agent

#  Step 2: Context for hotel
class HotelContext:
    def __init__(self, hotel: Optional[Literal["pearl", "crown", "one"]] = None):
        self.hotel = hotel


# Step 3: Dynamic instructions (change based on detected hotel)
def hotel_instructions(
    run_context: RunContextWrapper[HotelContext], agent: Agent[HotelContext]
) -> str:
    context = run_context.context

    if not context.hotel:
        return "Ask the user to specify which hotel (Pearl, Crown, or One)."

    hotel = hotels_data[context.hotel]
    return (
        f"You are a booking assistant for {hotel['name']} located in {hotel['location']}.\n"
        f"- Rooms: {hotel['rooms']}\n"
        f"- Facilities: {', '.join(hotel['facilities'])}\n"
        f"- Price Range: {hotel['price_range']}\n\n"
        "Answer only with details related to this hotel."
    )