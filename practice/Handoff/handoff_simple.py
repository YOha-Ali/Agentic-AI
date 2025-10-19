from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
gemini_api_key="AIzaSyBOeq8Wj1VnA0jQZRh35ZpnTZ2eVocCNVM"
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
math_assistant=Agent(
    name="Math assistant",
    instructions="You are a math expert asistant",
)
physics_assistant=Agent(
    name="Physics Assistant",
    instructions="You are a physics expert assistant",
)
chemistry_assistant=Agent(
    name="Chemistry Assistant",
    instructions="You are a chemistry expert assistant",
)
leader_assistant=Agent(
    name="Leader Assistant",
    instructions="You are a helpful assistant specialized in leadership and management.",
)
result=Runner.run_sync(starting_agent=leader_assistant, input="Tell me about history of Pakistan? in short please", run_config=config)
print(result.final_output)
# print(result.final_agent) 