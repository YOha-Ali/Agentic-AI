from agents import (
    Agent,
    GuardrailFunctionOutput,
    RunContextWrapper,
    input_guardrail,
    Runner
) 
from agent_config import config
@input_guardrail
async def math_guardrail(ctx:RunContextWrapper, agent:Agent, input:str)->GuardrailFunctionOutput:
    print(f"Guardrail is running with {input}")
    return GuardrailFunctionOutput(output_info="", tripwire_triggered=False)

agent=Agent(
    name="customer support agent",
    instructions="you are customer support agent, You help costumer with their questions",
    input_guardrails=[math_guardrail]
)
result=Runner.run_sync(
    agent,
    "Hello, can you help me solve x: 2x + 3 =11?",
    run_config=config
)
print(result.final_output) 