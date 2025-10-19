from agents import(
    Agent,
    GuardrailFunctionOutput,
    RunContextWrapper,
    input_guardrail,
    output_guardrail,
    Runner
)
from m_config import config

@input_guardrail
async def math_guardrail(wrapp:RunContextWrapper, abc:Agent, query:str)->GuardrailFunctionOutput:
    return GuardrailFunctionOutput(output_info="OK DONE", tripwire_triggered=False)

@output_guardrail
async def lenght_guardrail(wrapp:RunContextWrapper, abc:Agent, output:str)->GuardrailFunctionOutput:
    words = output.split()
    max_words = 50
    if len(words) > max_words:
        return GuardrailFunctionOutput(
            output_info="output too long", tripwire_triggered=True)
    return GuardrailFunctionOutput(output_info="Within lenght", tripwire_triggered=False)

@output_guardrail
async def offensive_words(wrapp:RunContextWrapper, abc:Agent, output:str)->GuardrailFunctionOutput:
    badwords=["idiot", "stupid", "dumb"]
    if any(word in output.lower() for word in badwords):
        return GuardrailFunctionOutput(output_info="offensive words detected", tripwire_triggered=True)
    return GuardrailFunctionOutput (output_info="No offensive words", tripwire_triggered=False)

agent=Agent(
    name="customer support agent",
    instructions="You are a polite support agent",
    input_guardrails=[math_guardrail],
    output_guardrails=[lenght_guardrail, offensive_words]
)
result=Runner.run_sync(agent, input="hey, how are you?", run_config=config)
print(result.final_output)