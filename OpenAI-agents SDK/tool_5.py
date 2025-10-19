from agents import Agent, Runner, function_tool, RunContextWrapper
from m_config import config 
from agents.exceptions import UserError
from typing_extensions import Any

def custom_function_error(ctx:RunContextWrapper[Any], error:Exception):
    """The default tool error function, which just return a generic error message."""
    return f"An error occurred while running the agent. Please try again {str(error)}" 

@function_tool(
        name_override="get_weather",
        description_override="weather ka data lay aoo",
        use_docstring_info=True,
        failure_error_function=custom_function_error
)

async def fetch_weather(city: str) -> str:
    """
    fetch weather according to the given city

    Args:
    city : city for fetching functions
    """
    # return f"The weather in {city} is sunny with 40C."
    raise UserError ("tool has error")

simple_agent = Agent(
    name="Simple Assistant",
    instructions="You are helpfull assistant",
    tools=[fetch_weather]
)

result = Runner.run_sync(
    simple_agent,
    input="what is the weather in karachi?", 
    run_config=config)
print("result>>>",result.final_output)