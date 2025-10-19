from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled

gemini_api_key = "AIzaSyClKLOVc-o6awnksGP3S_f3VF1iu08oxtw"

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_tracing_disabled(True)

agent = Agent(
    name="Pookie",
    instructions="You are very helpful",
    model=OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=client
    )
)

result = Runner.run_sync(
    agent,
    "Assalamualaikum! Python kya hota hai?"
)

print("RUN_SYNC:", result.final_output)