from agents import Agent, Runner, handoff, RunContextWrapper
from agent_config import config
from pydantic import BaseModel

clothing_assist=Agent(name="cloth assistent", instructions="You tell about all cloth fashion")
electronic_assist=Agent(name="electronic assistent", instructions="You tell about all electronic gadgets")

class DataFetch(BaseModel):
    reason:str

async def on_handoff_func(ctx:RunContextWrapper, input_data:DataFetch):
    print("Hand off with a reason:", input_data.reason)
    return f"\nReturn with {input_data.reason}"

# handoff_agent1=Agent(
#     agent=clothing_assist,
#     tool_name_override="clothing_specialized",
#     tool_descreption_override="You are specialized to know about all clothes fashion very well",
# )
# handoff_agent2=Agent(
#     agent=electronic_assist,
#     tool_name_override="electronics_specialized",
#     tool_descreption_override="You are specialized to know about all electronic gadgets very well",
# )

leader_agent=Agent(
    name="leader agent",
    handoffs=[
        electronic_assist,
        handoff(
            clothing_assist,
            on_handoff=on_handoff_func,
            input_type=DataFetch,
)])
result= Runner.run_sync(leader_agent, input="Tell me which is best, Prada or Fendi? and why", run_config=config)
print(result.final_output)
    