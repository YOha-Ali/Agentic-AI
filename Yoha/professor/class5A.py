from agents import Agent, Runner, function_tool
from my_config import config
from typing_extensions import TypedDict

mydatatype = TypedDict("mydatatype", {
    "name" : str,
    "city" : str,
    "age" : int
}) 

@function_tool
async def fetch_weather(city:str) -> str:
    """

    fetch weather according given City
    Args:

    city : city for weather
    """
    return f"The Weather in {city} is 40C"

simple_agent = Agent(
    name = "Munnu",
    instructions= "You are very helpful Munnu, give answer in Roman Urdu",
    tools=[fetch_weather]
)

result = Runner.run_sync(
    starting_agent=simple_agent,
    input = "what is 2 plus 2",
    run_config=config
)

print(result.final_output) 