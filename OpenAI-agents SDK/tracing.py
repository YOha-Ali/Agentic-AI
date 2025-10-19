from agents import Agent, Runner, trace
from m_config import config
import asyncio
async def main():
    agent=Agent(name="Joke generator", instructions="tell funny jokes")

    with trace("Joke workflow"):
        first_result= await Runner.run(agent, input="Tell me a joke", run_config=config)
        second_result=await Runner.run(agent, input=f"Rate this joke: {first_result.final_output}", run_config=config)
        print(f"Joke: {first_result.final_output}")
        print(f"Rating: {second_result.final_output}") 
asyncio.run(main())