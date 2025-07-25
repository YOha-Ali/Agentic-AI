from pydantic import BaseModel
from agents import (
    Agent,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    RunContextWrapper,
    input_guardrail,
    Runner
)
from my_config import config

@input_guardrail
async def math_guardrail(context:RunContextWrapper, agent:Agent, input:str) -> GuardrailFunctionOutput:
    print(f"Guardrail is running with input: {input}")
    return GuardrailFunctionOutput(output_info="", tripwire_triggered=False)

agent = Agent(
    name = "Customer support Agent",
    instructions="you are customer support agent, You help costumer with their questions",
    input_guardrails=[math_guardrail]
)

result = Runner.run_sync(
    agent,
    "Hello, can you help me solve x: 2x + 3 =11?",
    run_config=config
)

print(f"Result: {result.final_output}")
