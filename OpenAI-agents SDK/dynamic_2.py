from agents import RunContextWrapper, Agent, Runner
from m_config import config

def my_dynamic_instructions(context: RunContextWrapper, agent: Agent) -> str:
    return f"You are {agent.name}. You love helping people learn Python!"

agent = Agent(
    name="Python Helper",
    instructions=my_dynamic_instructions
)

result = Runner.run_sync(agent, "What is a function?", run_config=config)
print(result.final_output) 