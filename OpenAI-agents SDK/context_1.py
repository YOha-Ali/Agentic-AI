import asyncio
from dataclasses import dataclass
from m_config import config
from agents import Agent, RunContextWrapper, Runner, function_tool
@dataclass
class UserInfo:
    username:str
    uid:int
@function_tool
async def fetch_user_age(context:RunContextWrapper[UserInfo]):
    user=context.context
    return f"{user.username} is 23 years old"
async def main():
    user_info=UserInfo(username="YOha", uid=2345)
    agent = Agent[UserInfo](
        name="Assistent",
        instructions="You are a helpfull assistent. Always use the provided tools to answer questions about the user. And if they ask about my name and uid tell them also this",
        tools=[fetch_user_age])
    result= await Runner.run(agent, input="whats the name of the user?", context=user_info, run_config=config)
    print(result.final_output)
if __name__ == "__main__":
    asyncio.run(main())

