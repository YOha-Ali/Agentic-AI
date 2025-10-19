from agents import Agent, Runner
import asyncio
from m_config import config
agent=Agent(name="Helper", instructions="You are a helper")
async def main():
    runner= Runner(agent)
    result1= await runner.run("Introduce yourself", run_config=config)
    print(("Default:", result1))
    agent.instructions="You are a strict teacher. Answer very formally"
    result2= await runner.run("Introduce yourself", run_config=config)
    print("Dynamic:", result2)
asyncio.run(main()) 
