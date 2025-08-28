from dataclasses import replace
from agents import Agent, ModelSettings
from my_tools.tools import get_order_status
from my_guardrials.guardrial import block_negative_input

# Helper: enable the order tool only when our context says so.
def _order_tool_is_enabled(ctx, _agent):
    # ctx.context is our Pydantic SessionContext
    return bool(getattr(ctx, "context", None) and getattr(ctx.context, "order_tool_enabled", False))

# We can dynamically toggle tool availability by replacing the dataclass field
order_tool_enabled = replace(get_order_status, is_enabled=_order_tool_is_enabled)

BotAgent = Agent(
    name="BotAgent",
    instructions=(
        "You are a helpful customer support bot.\n"
        "- Answer common FAQs (support hours, returns, shipping, warranty) concisely.\n"
        "- For order tracking questions, call the `get_order_status` tool when it is available.\n"
        "- If the user is upset or requests a person, hand off to the human agent.\n"
        "- Always stay polite and positive."
    ),
    tools=[order_tool_enabled],  # dynamically enabled/disabled each run
    input_guardrails=[block_negative_input],
    model_settings=ModelSettings(
        tool_choice="auto",                 # let the model decide when to use tools
        metadata={"app": "support-bot"}     # sample metadata shown in docs
    ),
)

HumanAgent = Agent(
    name="HumanAgent",
    handoff_description="A human support representative who can handle complex or sensitive issues.",
    instructions=(
        "You are a human support representative. Take over with empathy, de-escalate if needed, "
        "ask for any missing details, and provide clear next steps."
    ),
)

# Allow BotAgent to hand off to HumanAgent
BotAgent.handoffs = [HumanAgent]
