import asyncio
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled

gemini_api_key="AIzaSyClKLOVc-o6awnksGP3S_f3VF1iu08oxtw"

client=AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
set_tracing_disabled(True)
async def main():
    agent=Agent(
        name="YOYO",
        instructions="You are a best friend of 'YOha',answer in roman urdu",
        model=OpenAIChatCompletionsModel(
            model="gemini-2.0-flash",
            openai_client=client
        )
    )
    result = await Runner.run(
        agent, 
        "mujhy koi cotaa sa joke batao"
    )
    print(result.final_output)
if __name__=="__main__":
    asyncio.run(main())