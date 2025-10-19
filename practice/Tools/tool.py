from agents import Agent, Runner, function_tool
from agent_config import config
import asyncio

@function_tool
async def fetch_weather(city:str)-> str:
    """Fetch weather according to the city
    Args:
    city: city for weather"""
    return f"The weather in {city} is rainy."

simple_agent=Agent(
    name="Weather handler Assistent",
    instructions="Tell about the weather all around the world",
    tools=[fetch_weather]
)
async def main():
    result= await Runner.run(
        simple_agent,
        input="whats the weather today?",
        run_config=config
    )
    print(result.final_output)
asyncio.run(main()) 