from agents import Agent, Runner, handoff, RunContextWrapper, function_tool
from agents.extensions import handoff_filters
from pydantic import BaseModel
import asyncio
from m_config import config

class HandoffData(BaseModel):
    summary:str

billing_agent = Agent(name="Billing agent", instructions="handling billing questions.")
technical_agent = Agent(name="technical agent", instructions="troubleshoot technical issues.")

def log_the_handoff(ctx:RunContextWrapper, input_data: HandoffData):
    print(f"\n[SYSTEM: Handoff initiated. Briefing: {input_data.summary}]\n")

to_billing_handoff= handoff(
    agent= billing_agent,
    tool_name_override="special_billing_agent",
    tool_description_override="know all billing query",
    on_handoff=log_the_handoff,
    input_type=HandoffData
)

to_technical_handoff= handoff(
    agent= technical_agent,
    tool_name_override="special_technical_agent",
    tool_description_override="know all technical query",
    on_handoff=log_the_handoff,
    input_type=HandoffData
)

@function_tool
def diagnose():
    return "The user's payment failed"

triage_agent= Agent(
    name="triage agent",
    instructions="First use the diagnose tool, Then, based on the issue, handoff to the correct specialist with a summary",
    tools=[diagnose],
    handoffs=[to_billing_handoff, to_technical_handoff]
)

async def main():
    result = await Runner.run(triage_agent, input="My payment wont go through", run_config=config)
    print(f"Final reply from: {result.last_agent}")
    print(f"Final message: {result.final_output}")
asyncio.run(main()) 