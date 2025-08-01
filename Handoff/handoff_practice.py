from agents import Agent, Runner, RunContextWrapper, handoff
from agent_config import config

billing_agent=Agent(name="billing agent")
refund_agent=Agent("refund agent")

billing_handoff=handoff(
    agent=billing_agent,
    tool_name_override="specialized_in_billing",
    tool_description_override="you are specialized in billing"
)

main_agent=Agent(
    name="main agent",
    instructions="You are main agent you will be given task and you have to handoff to the specialized agents accordingly",
    handoffs=[
        billing_handoff,
        refund_agent
    ]
)
result  = Runner.run_sync(
    starting_agent=main_agent,
    input="I am having some issue with my billing",
    run_config=config
)
print(result.final_output) 