
import os
import asyncio
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv() 
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

agent = genai.GenerativeModel("gemini-1.5-flash") 
prompt = input("Enter your prompt: ")

async def global_stream():
    print("\n[Global Level] stream()")
    stream = await genai.GenerativeModel(model_name="gemini-1.5-flash").generate_content_async(prompt, stream=True)
    async for chunk in stream:
        print(chunk.text, end="")

if __name__ == "__main__":
    asyncio.run(global_stream())
