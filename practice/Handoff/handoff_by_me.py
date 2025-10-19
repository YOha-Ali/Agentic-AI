from agents import Agent, Runner, handoff
from agent_config import config
next_js_assistant=Agent(name="Next js Assistant") 
python_assistant=Agent(name="Python Assistant")
triage_agent=Agent(name="Triage agent", handoffs=[handoff(next_js_assistant), handoff(python_assistant)])
result= Runner.run_sync(starting_agent=triage_agent, input="Tell me about python decorators in short.", run_config=config)
print(result.final_output) 