from agents import Agent, Runner
from m_config import config

spanish_agent=Agent(name="spanish agent", instructions="you are a spanish translator")
arabic_agent=Agent(name="arabic agent", instructions="you are a arabic translator")

orchestrating_agent=Agent(
    name="orchestrator_agent",
    instructions="When the user asks for a translation, choose the correct tool (Spanish or Arabic) and provide the translation.",
    tools=[
        spanish_agent.as_tool(
            tool_name="spanish_translator",
            tool_description="translate user message into spanish"
        ),
        arabic_agent.as_tool(
            tool_name="arabic_translator",
            tool_description="you translate user message into arabic"
        )
    ]
)
result = Runner.run_sync(orchestrating_agent, input="what is 3675 + 678?", run_config=config)
print(result.final_output)

