from pydantic import BaseModel
from agents import (
    Agent,
    GuardrailFunctionOutput,
    OutputGuardrailTripwireTriggered,
    RunContextWrapper,
    Runner,
    output_guardrail,
)
from dotenv import load_dotenv
import asyncio

load_dotenv()

class MessageOutput(BaseModel): 
    response: str

class PoliticalContentCheck(BaseModel):
    contains_politics: bool
    reasoning: str

politics_detector = Agent(
    name="Politics Detector",
    instructions=(
        "Check whether the assistant's response includes political content or mentions political figures. "
        "Return `contains_politics: True` if detected, else False."
    ),
    output_type=PoliticalContentCheck,
)

output_guardrail
async def avoid_politics_output(  
    ctx: RunContextWrapper, 
    agent: Agent, 
    output: MessageOutput
) -> GuardrailFunctionOutput:
    # Check the agent's response for sensitive content
    result = await Runner.run(
        politics_detector, 
        f"Please analyze this customer service response: {output.response}", 
        context=ctx.context
    )
    
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.contains_politics
    )

support_agent = Agent( 
    name="Customer Support Agent",
    instructions="Help customers with their questions. Be friendly and informative.",
    output_guardrails=[avoid_politics_output],  # Add our privacy check
    output_type=MessageOutput,
)

async def main():
    try:
        # This might generate a response with sensitive info
        result = await Runner.run(
            support_agent, 
            "Who is the prime minister of Pakistan"
        )
        print(f"✅ Response approved: {result.final_output.response}")
    
    except OutputGuardrailTripwireTriggered as e:
        print("🛑 Response blocked - avoid politics!")

print(asyncio.run(main()))


