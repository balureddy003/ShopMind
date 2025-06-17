import os
from typing import Any, Dict

import httpx

BASE_URL = os.environ.get("GRANDNODE_URL", "http://grandnode:5000")


class GrandNodeClient:
    def __init__(self, api_key: str | None = None):
        self.client = httpx.AsyncClient(base_url=BASE_URL, headers={"ApiKey": api_key} if api_key else None)

    async def add_to_cart(self, product_id: str, quantity: int = 1) -> Dict[str, Any]:
        resp = await self.client.post("/api/cart/addproduct", json={"productId": product_id, "quantity": quantity})
        resp.raise_for_status()
        return resp.json()

    async def checkout(self) -> Dict[str, Any]:
        resp = await self.client.post("/api/order/checkout")
        resp.raise_for_status()
        return resp.json()

    async def order_status(self, order_id: str) -> Dict[str, Any]:
        resp = await self.client.get(f"/api/order/{order_id}")
        resp.raise_for_status()
        return resp.json()
