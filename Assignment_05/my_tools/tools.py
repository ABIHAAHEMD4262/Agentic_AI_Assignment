from agents import function_tool

@function_tool
def add(a:int, b:int):
    """function take 2 input a and b and return a + b"""
    print("Add Function Called ----->")
    return a + b

@function_tool
def get_weather(city:str) -> str:
    print("Weather function fired---->")
    """Returns mock weather info for the given city."""
    return f"The current temperature in any {city} is 34 ℃ with clear skies."