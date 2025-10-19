from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, set_default_openai_api

gemini_api_key = "AIzaSyDF91icM5MWB7Bkio4aURuwoxN3efdW_7A"
set_tracing_disabled(True) 
set_default_openai_api("chat_completions")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
set_default_openai_client(external_client)

agent: Agent = Agent(name="Pookie", instructions="You are Pookie. speak in roman urdu. I am Yoha Ali Azam", model="gemini-2.0-flash")

result = Runner.run_sync(agent, "headache horaha h kya karun?") 

print(result.final_output)