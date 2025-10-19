from agents import(
    Agent,
    GuardrailFunctionOutput,
    RunContextWrapper,
    input_guardrail,
    output_guardrail,
    Runner
)
from m_config import config
from agents.exceptions import OutputGuardrailTripwireTriggered

@input_guardrail
async def math_guardrail(
    context: RunContextWrapper, agent:Agent, input:str
) -> GuardrailFunctionOutput:
    print(f"guardrail is running with {input}")
    return GuardrailFunctionOutput(
        output_info="OK",
        tripwire_triggered=False
    )
# @output_guardrail
# async def math_output(
#     context:RunContextWrapper, agent:Agent, output:str)->GuardrailFunctionOutput:
#     print(f"guardrail is running with {output}")
#     return GuardrailFunctionOutput(
#         output_info="I only answer with math problems.",
#         tripwire_triggered=True
    # )

agent = Agent(
    name="Customer support agent",
    instructions="You only answer math questions, never answer anything else",
    input_guardrails=[math_guardrail],
    # output_guardrails=[math_output]
)
try:
    result = Runner.run_sync(agent, input="Hello, can you tell me about python in short?", run_config=config)
    print(result.final_output)

except OutputGuardrailTripwireTriggered as e:
    print("⚠️ Output blocked by guardrail:", e)


