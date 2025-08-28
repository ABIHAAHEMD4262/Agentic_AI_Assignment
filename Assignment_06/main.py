
from dotenv import load_dotenv
from agents import Runner,set_tracing_disabled
from my_models.models import SessionContext
from my_agents.agents import BotAgent

load_dotenv()  # expects OPENAI_API_KEY for OpenAI models
set_tracing_disabled(True)


FAQ_KEYWORDS = ("support hours", "hours", "warranty", "refund", "return", "shipping")
ORDER_KEYWORDS = ("order", "track", "status", "shipment", "delivery", "ord-")


def infer_order_mode(text: str) -> bool:
    """Check if the user query is related to orders."""
    t = text.lower()
    return any(k in t for k in ORDER_KEYWORDS)


def main():
    print("🤖 Support Bot (Agents SDK) — type 'exit' to quit\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("👋 Goodbye!")
            break

        # Toggle the order tool only when relevant to the query
        ctx = SessionContext(
            customer_id="CUST-001",
            order_tool_enabled=infer_order_mode(user_input)
        )

        try:
            result = Runner.run_sync(
                BotAgent,
                user_input,
                context=ctx
            )
            print("Bot:", result.final_output)

        except Exception as e:
            # Guardrail triggered OR any runtime error
            if "Guardrail InputGuardrail triggered" in str(e):
                print("Bot: ⚠️ I cannot respond to abusive or unsafe language.")
            else:
                print("Bot: ⚠️ Something went wrong while processing your request.")


if __name__ == "__main__":
    main()
