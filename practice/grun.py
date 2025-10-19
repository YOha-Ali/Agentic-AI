from agents import Agent, AsyncOpenAI, Runner, set_default_openai_api, set_tracing_disabled, set_default_openai_client

gemini_api_key="AIzaSyBOeq8Wj1VnA0jQZRh35ZpnTZ2eVocCNVM"
set_tracing_disabled(True)
set_default_openai_api("chat_completions")
client=AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
set_default_openai_client(client)
agent=Agent(name="YOYO", instructions="You are a polite helpful assistant and your name is 'YOYO'", model="gemini-2.0-flash")
result=Runner.run_sync(agent, "YOYO koi achi baat batao in roman urdu")
print(result.final_output)