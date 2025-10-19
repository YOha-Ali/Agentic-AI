from agents import Agent, Runner, RunContextWrapper, FunctionTool 
from pydantic import BaseModel
from m_config import config

def do_some_work(data:str):
    return f"Proceed: {data}"

class FunctionArgs(BaseModel):
    username : str
    age : int

async def run_function(ctx:RunContextWrapper, args:str):
    parsed= FunctionArgs.model_validate_json(args)
    return do_some_work(data=f"{parsed.username} is {parsed.age} years old.")

process_user_tool= FunctionTool(
    name="process_user",
    description="Processes extracted user data",
    params_json_schema=FunctionArgs.model_json_schema(),
    on_invoke_tool=run_function
)

agent=Agent(
    name="custom_tool_agent",
    instructions="You can process user info using a tool",
    tools=[process_user_tool]
)
result = Runner.run_sync(
    agent,
    input="Please process user YOHA with age 23",
    run_config=config
)
print(result.final_output)