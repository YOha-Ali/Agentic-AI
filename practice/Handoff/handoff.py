from agents import Agent, Runner, handoff, RunContextWrapper
from agent_config import config
from pydantic import BaseModel

python_assist=Agent(name="python assistent", instructions="You are a helpful assistent in python only")
nextjs_assist=Agent(name="next js assistent", instructions="You are a helpful assistent in nextjs only")

class EscalationData(BaseModel):
    reason:str

async def on_handoff(abc:RunContextWrapper, input_data:EscalationData):
    print("Hand off called with reason", input_data.reason)

python_handoff=handoff(
    agent=python_assist,
    tool_name_override="python_specialized",
    tool_description_override="you are specialized in python",
    input_type=EscalationData,
    on_handoff=on_handoff
)
nextjs_handoff=handoff(
    agent=nextjs_assist,
    tool_name_override="nextjs_specialized",
    tool_description_override="you are specialized in nextjs",
    input_type=EscalationData,
    on_handoff=on_handoff
)

leader=Agent(name="Leader Assistent",
             instructions="You are Lead agent you will be given task and you have to handoff to the specialized agents accordingly",
             handoffs=[python_handoff, nextjs_handoff]) 

result = Runner.run_sync(leader, input="tell me about python decoretor", run_config=config)
print(result.final_output) 