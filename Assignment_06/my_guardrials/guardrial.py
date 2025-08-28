from typing import Any
from agents import input_guardrail, GuardrailFunctionOutput

_BAD_WORDS = {
    "stupid", "idiot", "dumb", "hate", "suck", "ugly",
    "trash", "useless", "worst", "fool"
}

@input_guardrail()
def block_negative_input(_ctx, _agent, user_input: Any) -> GuardrailFunctionOutput:
    """
    Blocks clearly negative/offensive input and returns a polite warning.
    Works for string input (CLI) and generic list-like inputs.
    """
    text = user_input if isinstance(user_input, str) else " ".join(map(str, user_input))
    lowered = text.lower()

    if any(w in lowered for w in _BAD_WORDS):
        return GuardrailFunctionOutput(
            tripwire_triggered=True,
            output_info={"warning": "Please keep it respectful. We can connect you to a human if needed."}
        )

    # ✅ must provide output_info even if empty
    return GuardrailFunctionOutput(
        tripwire_triggered=False,
        output_info={}
    )
