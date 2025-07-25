from agents import Agent, Runner, function_tool, RunContextWrapper
from my_config import config
from typing_extensions import TypedDict
from dataclasses import dataclass

@dataclass
class Userinfo:
    name : str
    designation : str

local_context = Userinfo(name="YOha", designation="Professor")

class ContextType(TypedDict):
    name : str
    description : str

local_context = {
    "name" : "YOha",
    "designation" : "Professor"
}

@function_tool
async def fetch_weather(wrapper:RunContextWrapper, city:str) -> str:
    """

    fetch weather according given City
    Args:

    city : city for weather
    """
    print("context>>>", wrapper.context["name"])
    user_name = wrapper.context["name"]
    return f"Hi {user_name} The weather in {city} is sunny."

simple_agent = Agent(
    name="Assistant",
    instructions="You are helpful assistant",
    tools=[fetch_weather]
)

result = Runner.run_sync(
    starting_agent=simple_agent,
    input = "what is 2 plus 22",
    run_config=config,
    context=local_context
)

print(result.final_output)