from agents import Agent, Runner,ItemHelpers, function_tool
import asyncio, random
from m_config import config
from openai.types.responses import ResponseTextDeltaEvent
@function_tool
async def how_many_jokes(joke: str):
    print("telling a joke")
    return joke
simple_agent = Agent(
        name="Simple Assistant",
        instructions="You are helpfull assistant, First, determine how many jokes to tell, then provide jokes.",
        tools=[how_many_jokes])
async def main():
    result = Runner.run_streamed(simple_agent,input= "Hi?", run_config=config)

    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data,ResponseTextDeltaEvent):
            print("Events:", event)
            print(event.data.delta, end="")
            continue
        elif event.type == "agent_updated_stream_event":
            print("event>>>>:", event)
            print(f"Agent updated with {event.new_agent.name}")
            

asyncio.run(main()) 



