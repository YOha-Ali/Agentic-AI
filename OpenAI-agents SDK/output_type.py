from pydantic.dataclasses import dataclass
from agents import Agent, Runner
from m_config import config

@dataclass
class UserInfo:
    name: str
    designation: str

# ✅ output_type diya
user_agent = Agent[UserInfo](
    name="UserAgent",
    instructions="Extract name and designation.",
    output_type=UserInfo
)

result = Runner.run_sync(user_agent, input="My name is Ali and I am a Teacher.", run_config=config)
print(result)
