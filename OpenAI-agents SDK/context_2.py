from agents import Agent, Runner,function_tool,RunContextWrapper
from m_config import config
from pydantic import BaseModel

class UserInfo(BaseModel): 
    name: str
    designation: str

local_context = UserInfo(name="YOha",designation="Teacher")

def dynamic_instructions(wrapper:RunContextWrapper[UserInfo], agent:Agent[UserInfo]) -> str:
    # user_name = wrapper.context["name"]
    return f"The user's name is {wrapper.context.name}. Help them with their questions."

simple_context_agent = Agent[UserInfo](
    name="Context Agent",
    instructions=dynamic_instructions
)
result = Runner.run_sync(
    simple_context_agent,
    "what is the name of the user?", 
    run_config=config,
    context=local_context,    
    )
print("result>>>>",result.final_output)