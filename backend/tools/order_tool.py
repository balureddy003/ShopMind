from typing import Any, Dict
from autogen import Tool
from .grandnode_client import GrandNodeClient


class GrandNodeOrderTool(Tool):
    def __init__(self, client: GrandNodeClient):
        super().__init__(name="order_tool", description="Checkout and order status")
        self.client = client

    async def checkout(self) -> Dict[str, Any]:
        return await self.client.checkout()

    async def status(self, order_id: str) -> Dict[str, Any]:
        return await self.client.order_status(order_id)
