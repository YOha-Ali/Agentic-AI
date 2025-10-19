# import asyncio
# from openai import AsyncOpenAI 
# from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled

# gemini_api_key = "AIzaSyClKLOVc-o6awnksGP3S_f3VF1iu08oxtw"

# client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )

# set_tracing_disabled(True)

# async def main():
#     agent = Agent(
#         name = "Pookie",
#         instructions = "You are very helpful plus attitude assistant",
#         model = OpenAIChatCompletionsModel(
#             model="gemini-2.0-flash",
#             openai_client=client
#         )
#     )
#     result = await Runner.run(
#         agent,
#         "Assalamualikum, kiya haal hain?", 
#     )
#     print(result.final_output)

# if __name__ == "__main__":
#     asyncio.run(main())

