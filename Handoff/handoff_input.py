from agents import Agent, Runner,handoff, RunContextWrapper
from agent_config import config
from pydantic import BaseModel
import asyncio
class EscalationData(BaseModel):
    reason:str
async def on_handoff(ctx:RunContextWrapper[EscalationData], input_data:EscalationData):
    print(f"Escalation agent called with reason: {input_data.reason}")
    return f"Escalated to another agent because: {input_data.reason}"
escal_agent=Agent(name="Escalation agent")
handoff_obj=handoff(
    agent=escal_agent,
    on_handoff=on_handoff,
    input_type=EscalationData,)
parent_agent=Agent(
    name="Support Agent",
    instructions="""
    You are helpful support assistant
    If the user mentions handoff or escalation, call the handoff with a reason.
    """)
allowed_tools=[escal_agent]
result= asyncio.run(Runner.run(starting_agent=parent_agent, input="Please escalate this issue. I want to talk to your manager.", run_config=config))
print(result.final_output) 
