from agents import Agent, Runner, function_tool, RunContextWrapper
from agent_config import config
from pydantic import BaseModel
from typing_extensions import TypedDict
import asyncio
class UserInfo(BaseModel):
    name : str
    age : int
    alive : bool
    seat_no : int
user = UserInfo(name="YOha", age=22, seat_no=7890)
user={
    "name":"YOha",
    "age":22,
    "seat_no":7890
}
@function_tool
async def user_introduce(wrapper:RunContextWrapper[UserInfo])->str:
    user_info=wrapper.context
    return f"Hi! My name is {user_info.name} and I am {user_info.age} years old, this is my {user_info.seat_no}."
async def main():    
    simple_agent=Agent(
        name="Info Agent",
        instructions="You have all information, so If someone asks about the user, use the tool to introduce them.",
        tools=[user_introduce]
    )
    result = await Runner.run(
        simple_agent,
        input="what is user name?",
        run_config=config,
        context=user
    )
    print(result.final_output) 
asyncio.run(main()) 