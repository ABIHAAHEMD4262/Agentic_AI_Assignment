from pydantic import BaseModel
from typing import Optional

class SessionContext(BaseModel):
    customer_id: Optional[str] = None
    # We’ll flip this per message so the LLM only sees the order tool when relevant
    order_tool_enabled: bool = False
