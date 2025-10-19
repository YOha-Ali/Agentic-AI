from agents import Agent, Runner 
from m_config import config
from pydantic import BaseModel

class PersonInfo(BaseModel):
    name:str
    age:int
    occupation:str

agent=Agent(
    name="Assistent",
    instructions="Extract person information from the user's message.",
    output_type=PersonInfo
)

result= Runner.run_sync(
    agent, 
    input="HI, My name is YOha, I am 23 years old and I am a Teacher.",
    run_config=config)
print("Type:", type(result.final_output))
print(result.final_output.name)
print(result.final_output.age)
print(result.final_output.occupation)