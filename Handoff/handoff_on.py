from agents import Agent, Runner, RunContextWrapper, handoff
from agent_config import config

def on_handoff(ctx: RunContextWrapper[None]):
    print("Handoff called")

agent=Agent(name="My agent")

handoff_obj=handoff(
    agent=agent,
    on_handoff=on_handoff,
    tool_name_override="coustom_handoff_tool",
    tool_description_override="custom description"
)
parent_agent=Agent(
    name="Support Agent",
    instructions="""
    You are helpful support assistant
    If the user mentions handoff or escalation, call the handoff with a reason.
    """,
    handoffs=[handoff_obj]
)
result= Runner.run_sync(starting_agent=parent_agent, input="Please escalate this issue. I want to talk to your manager.", run_config=config)
print(result.final_output)  
