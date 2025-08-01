from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, handoff
from agents.run import RunConfig
gemini_api_key="AIzaSyClKLOVc-o6awnksGP3S_f3VF1iu08oxtw"
client=AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
model=OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client,
)
config=RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True,
)
next_js_assistant=Agent(name="Next js Assistant") 
python_assistant=Agent(name="Python Assistant")
triage_agent=Agent(name="Triage agent", handoffs=[handoff(next_js_assistant), handoff(python_assistant)])
result= Runner.run_sync(starting_agent=triage_agent, input="Tell me about next js", run_config=config)
print(result.final_output) 