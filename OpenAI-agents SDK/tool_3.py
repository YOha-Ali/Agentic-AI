from agents import  Agent, Runner, function_tool, StopAtTools
import asyncio
from m_config import config

@function_tool
def get_user_data(user_id:str):
    """looks up user data"""
    return f"Data for {user_id}: Name - YOHa, Role - user"

@function_tool
def delete_user(user_id:str):
    """deletes a user. this is a final action"""
    return f"user {user_id} has been deleted"

admin_agent=Agent(
    name= "admin agent",
    instructions="help manage user, first get data, then delete it, if asked",
    tools=[get_user_data, delete_user],
    tool_use_behavior=StopAtTools(tools_to_stop=["get_user_data"]) 
)

async def main():
    print("------ Running as a regular agent------")
    result_user= await Runner.run(
        admin_agent, 
        input="Please delete user client_456", 
        context={"role":"user"},
        run_config=config)
    print(f"Final output: {result_user.final_output}")

    print("\n------ Running as admin-----")
    result_admin= await Runner.run( 
        admin_agent, 
        input="get data for user_123 and then delete them", 
        context={"role":"admin"}, 
        max_turns=1,
        run_config=config) 
    print(result_admin.final_output)
asyncio.run(main())