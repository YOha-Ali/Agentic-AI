import asyncio
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, Runner

gemini_api_key = "AIzaSyBOeq8Wj1VnA0jQZRh35ZpnTZ2eVocCNVM"

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)

agent: Agent = Agent(name="Yo", instructions="You are 'Yo' and your best friend name is 'Yoha' answer in roman urdu")

result = asyncio.run(Runner.run(starting_agent=agent, input="Kya kar rahy ho Yo?", run_config=config))
print(result.final_output)