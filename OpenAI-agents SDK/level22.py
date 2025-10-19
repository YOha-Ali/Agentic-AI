from agents import Agent, Runner, function_tool, ModelSettings
from pydantic import BaseModel
from m_config import config

# ------------------------------
# Tool 1: Add Numbers
# ------------------------------
@function_tool
def add_numbers(x: int, y: int) -> int:
    """Add two numbers together"""
    return x + y

# ------------------------------
# Tool 2: Get Weather
# ------------------------------
class WeatherInput(BaseModel):
    location: str
    unit: str = "C"

@function_tool
def get_weather(data: WeatherInput) -> dict:
    """Fetch current weather info"""
    return {"location": data.location, "temperature": 30, "unit": data.unit}

# ------------------------------
# Agent Setup
# ------------------------------
agent = Agent(
    name="DemoAgent",
    instructions="You are a helpful assistant. Use tools to answer questions.",
    tools=[add_numbers, get_weather] , # tools list me add kar diye
    model_settings=ModelSettings(tool_choice="required")
)

# ------------------------------
# Runner with run_sync()
# ------------------------------

# Example 1: Add numbers
# result1 = Runner.run_sync(agent, input="Add 10 and 15", run_config=config)
# print("Result 1:", result1.final_output)

# Example 2: Weather
result2 = Runner.run_sync(agent, input="What's the weather in Karachi?", run_config=config) 
print("Result 2:", result2.final_output)
