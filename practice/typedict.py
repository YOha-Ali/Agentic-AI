from agents import Agent, Runner
from typing_extensions import TypedDict
from agent_config import config
class MyMath(TypedDict):
    num1 : int
    num2 : int
    sum : int
agent=Agent(
    name="Math Assistant",
    instructions="Tum ek assistant ho jo do numbers ka sum structured format mein return karta hai.",
    output_type=MyMath 
)
result = Runner.run_sync(starting_agent=agent, input="what is 267 + 8438", run_config=config)
for key, value in result.final_output.items():
    print(f"{key.capitalize()} : {value}")
print(type(result.final_output)) 
