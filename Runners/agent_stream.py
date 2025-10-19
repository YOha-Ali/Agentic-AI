import os
import asyncio
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv() 
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

agent = genai.GenerativeModel("gemini-1.5-flash") 
prompt = input("Enter your prompt: ")

async def agent_stream():
    print("\n[Agent Level] stream()")
    stream = await agent.generate_content_async(prompt, stream=True)
    async for response in stream:
        print(response.text)

if __name__ == "__main__":
    asyncio.run(agent_stream())