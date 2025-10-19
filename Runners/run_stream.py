
import os
import asyncio
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv() 
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

agent = genai.GenerativeModel("gemini-2.0-flash") 
prompt = input("Enter your prompt: ")

async def run_stream():
    print("\n[Run Level] stream()")
    model = genai.GenerativeModel("gemini-1.5-flash")
    stream = await model.generate_content_async(prompt, stream=True)
    async for chunk in stream:
        print(chunk.text, end="")

if __name__ == "__main__":
    asyncio.run(run_stream())
