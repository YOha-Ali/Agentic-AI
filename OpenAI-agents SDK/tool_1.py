from agents import Agent, Runner, function_tool
from m_config import config

@function_tool
async def fetch_weather(city:str):
    """
    You tell the weather according to the city
    """
    return f"The weather in {city} is sunny"

agent=Agent(
    name="weather assistent",
    instructions="you tell about weather",
    tools=[fetch_weather]
)
result = Runner.run_sync(agent, input="whats the weather in karachi?", run_config=config)
print(result.final_output)