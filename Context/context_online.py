from agents import Agent, Runner, function_tool, RunContextWrapper
import asyncio
from agent_config import config
from dataclasses import dataclass
# informatin in tools and API key is a local context which LLM dont read
# sys prompt, instructions and user input are LLM/Agent context
@dataclass
class UserInfo:
    name        : str
    roll_number : int

@function_tool
                                                # data class name
async def fetch_user_profession(wrapper: RunContextWrapper[UserInfo])->str:
    return f"User {wrapper.context.name} is a Professor" 
# Now we make a object of context 
async def main():
#   obj name=call class here
    user_info=UserInfo(name="YOha", roll_number=1234)
    agent=Agent[UserInfo](
        name="Baady Bhai",
        instructions="You have access to the user's information. If anyone asks about them, use the tool to answer.",
        tools=[fetch_user_profession] 
    )
    result = await Runner.run(
        starting_agent=agent, 
        input="what is the profession of the user?",
        context=user_info, # put obj name here, not a class name
        run_config=config)
    print(result.final_output) 
if __name__ == "__main__":
    asyncio.run(main()) 