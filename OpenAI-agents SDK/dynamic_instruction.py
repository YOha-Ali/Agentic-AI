from agents import Agent, Runner, RunContextWrapper
from pydantic import BaseModel
from m_config import config

class UserContext(BaseModel):
    id: int
    name: str

user = UserContext(name='Ali', id=123)

def dynamic_instructions(
    context: RunContextWrapper[UserContext], agent: Agent[UserContext]
) -> str:
    return f"The user's name is {context.context.name}. Help them with their questions."

agent = Agent[UserContext](
    name="Triage agent",
    instructions=dynamic_instructions,
)

result = Runner.run_sync(
    starting_agent=agent,
    input="What is the name of the user?",
    context=user,
    run_config=config
)

print(result.final_output)