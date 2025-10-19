# # # def main():
# # #     print("Hello from hello world")


# # # print("__name__", __name__)
# # # if __name__=="__main__": # name guard, to run file direct
# # #     main()

# from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
# from agents.run import RunConfig

# gemini_api_key = "AIzaSyClKLOVc-o6awnksGP3S_f3VF1iu08oxtw"

# #Reference: https://ai.google.dev/gemini-api/docs/openai
# client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )

# model = OpenAIChatCompletionsModel(
#     model="gemini-2.0-flash",
#     openai_client=client
# )

# config = RunConfig(
#     model=model,
#     model_provider=client,
#     tracing_disabled=True
# )

# agent: Agent = Agent(name="Assistant", instructions="You are a helpful assistant")

# result = Runner.run_sync(starting_agent=agent, input="just tell me the name of best horror movies in hindi dubbed?", run_config=config)

# print(result.final_output) 



# from dotenv import load_dotenv
# import os
# import google.generativeai as genai

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# print("API KEY:", api_key)  # Debug print

# genai.configure(api_key=api_key)
