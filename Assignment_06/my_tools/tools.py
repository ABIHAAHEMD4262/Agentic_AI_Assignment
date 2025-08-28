from typing import Any, Dict
from dataclasses import replace
from agents import function_tool  # decorator returns a FunctionTool
from datetime import date

# --- a tiny in-memory "DB"
_ORDER_DB: Dict[str, Dict[str, str]] = {
    "ORD-1001": {"status": "Shipped",    "eta": "2025-08-30"},
    "ORD-1002": {"status": "Processing", "eta": "2025-09-02"},
    "ORD-1003": {"status": "Delivered",  "eta": "2025-08-26"},
}

def _friendly_error(prefix: str):
    # matches ToolErrorFunction signature: (tool_context, exception) -> str
    def make(ctx: Any, e: Exception) -> str:
        return f"{prefix}: {str(e)}"
    return make

@function_tool(
    failure_error_function=_friendly_error("⚠️ Order lookup error")
)
def get_order_status(order_id: str) -> str:
    """
    Fetches the order status for an ID mentionin the _ORDER_DB.
    Returns a short, friendly sentence with status and ETA.
    """
    data = _ORDER_DB.get(order_id.strip().upper())
    if not data:
        raise ValueError("Order not found. Please check the ID (e.g., ORD-1001).")
    return f"Order {order_id.upper()} is {data['status']} (ETA: {data['eta']})."
