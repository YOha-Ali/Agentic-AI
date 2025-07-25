from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

gemini_api_key = "AIzaSyClKLOVc-o6awnksGP3S_f3VF1iu08oxtw"

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

next_js_assistant = Agent(
    name="Next.js Assistant", 
    instructions="You are a helpful assistant specialized in Next.js development."
)
python_assistant = Agent(
    name="Python Assistant", 
    instructions="You are a helpful assistant specialized in Python programming."
)  

leader_assistant = Agent(
    name="Leadership Assistant", 
    instructions="You are a helpful assistant specialized in leadership and management."
)

result = Runner.run_sync(starting_agent=leader_assistant, input= "Tell me about python", run_config=config)

print(result.last_agent)
print(result.final_output)





# def main():
#     print("Hello from professor!")


# if __name__ == "__main__":
#     main()
