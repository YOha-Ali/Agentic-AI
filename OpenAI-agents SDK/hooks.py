import asyncio
from agents import Agent, Runner, RunContextWrapper, handoff, AgentHooks
from m_config import config
class MyAgentHooks(AgentHooks):
    async def oh_handoff(self, ctx:RunContextWrapper, agent:Agent, source:Agent):
        print(f"[AgentHooks] {agent.name} received handoff from {source.name}")
greeter = Agent(
    name="GreeterAgent",
    instructions="Greet the user and handoff.")
helper = Agent(
    name="HelperAgent",
    instructions="Answer the question after receiving handoff.")
helper.hooks = MyAgentHooks()
async def greeter_logic(ctx:RunContextWrapper, agent:Agent, inp:str):
    print(f"[Greeter Logic] Hello! Passing to HelperAgent...")
    return handoff(to_agent= helper, input_data=inp)
greeter.logic = greeter_logic
async def main():
    result = await Runner.run(greeter, "what is 22+77?", run_config=config)
    print(result)
asyncio.run(main())