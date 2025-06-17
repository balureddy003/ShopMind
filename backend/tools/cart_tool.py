from typing import Any, Dict
from autogen import Tool
from .grandnode_client import GrandNodeClient


class GrandNodeCartTool(Tool):
    def __init__(self, client: GrandNodeClient):
        super().__init__(name="add_to_cart", description="Add product to cart")
        self.client = client

    async def call(self, product_id: str, quantity: int = 1) -> Dict[str, Any]:
        return await self.client.add_to_cart(product_id, quantity)
