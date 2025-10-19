from agents import Agent, Runner, function_tool, ModelSettings
from m_config import config
from typing_extensions import TypedDict

@function_tool
def get_weather(city:str):
    """Tell the weather according to the city"""
    print("Get weather>>>")
    return f"The weather in {city} is Sunny."

@function_tool
def calculator(num1:int, num2:int):
    """"Sum the given numbers"""
    print("Calculated>>>")
    return num1 + num2
class MySum(TypedDict):
    num1:int
    num2:int
    sum:int
agent=Agent(
    name="Asssistent",
    instructions="You are a helpful assistent, help the user by using tools , where needed",
    tools=[get_weather, calculator],
    model_settings=ModelSettings(tool_choice="auto",
                                 parallel_tool_calls=True),
    output_type=MySum
)
jawab= Runner.run_sync(agent, input="what is the weather in US and what is 789+534?", run_config=config)
print(jawab.final_output) 