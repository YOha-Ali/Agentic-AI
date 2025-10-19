from agents import Agent, OpenAIChatCompletionsModel, AsyncOpenAI, Runner, set_tracing_disabled

gemini_api_key="AIzaSyBOeq8Wj1VnA0jQZRh35ZpnTZ2eVocCNVM"

client=AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
set_tracing_disabled(True)

agent=Agent(
        name="YOYO",
        instructions="You are a lovely helpful 'YOYO' a best friend of YOha, answer in Roman Urdu",
        model=OpenAIChatCompletionsModel(
            model="gemini-2.0-flash",
            openai_client=client
        )
    )
result= Runner.run_sync(
    agent,
    "koi Sunnat batado"
)
print(result.final_output)
