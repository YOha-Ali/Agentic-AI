from agents import Agent, Runner
from agent_config import config
import asyncio

spanish_agent=Agent(name="spanish agent",instructions="You are a Spanish translator. Translate anything given to you into Spanish.")
french_agent=Agent(name="french agent",instructions="You are a French translator. Translate anything given to you into French.")
arabic_agent=Agent(name="arabic_agent",instructions="You are a Arabic translator. Translate anything given to you into Arabic.")

orchestrator_agent=Agent(
    name="ochestrator_agent",
    instructions=(
        "You are translation agent. You use the tools givent to you, "
        "If asked for multiple translations, you call the relevant tools"
    ),
    tools=[
        spanish_agent.as_tool(
            tool_name="spanish_translator",
            tool_description="you translate a user message into spanish"
        ),
        french_agent.as_tool(
            tool_name="french_translator",
            tool_description="translate a user message into french"
        ),
        arabic_agent.as_tool(
            tool_name="arabic_translator",
            tool_description="Translate user message into Arabic"
        )
    ]
)
async def main():
    result = await Runner.run(
        starting_agent=orchestrator_agent,
        input="Say 'Hello! How are you?' in French",
        run_config=config
    )
    print(result.final_output)
asyncio.run(main()) 