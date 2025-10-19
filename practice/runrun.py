import asyncio
from agents import Agent, OpenAIChatCompletionsModel, Runner
from openai import AsyncOpenAI
from agents.run import RunConfig

gemini_api_key="AIzaSyBOeq8Wj1VnA0jQZRh35ZpnTZ2eVocCNVM"
client=AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.c" \
    "om/v1beta/openai/",
)
model=OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=client
)
config=RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)
agent=Agent(
    name="YOYO", 
    instructions="You are a lovely answerable agent in roman urdu"
) 
async def main():
    result = await Runner.run(agent, "kiya haal h YOYO?", run_config=config)
    print(result.final_output)
asyncio.run(main())