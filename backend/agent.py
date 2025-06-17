from __future__ import annotations
import os
from typing import AsyncIterable

from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

from .tools.cart_tool import GrandNodeCartTool
from .tools.order_tool import GrandNodeOrderTool
from .tools.grandnode_client import GrandNodeClient


OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://ollama:11434/v1")
CONFIG_LIST = [
    {
        "model": "llama3",
        "api_base": OLLAMA_URL,
        "api_type": "openai",
        "api_key": "none",
    }
]


def create_agent() -> AssistantAgent:
    client = GrandNodeClient()
    cart_tool = GrandNodeCartTool(client)
    order_tool = GrandNodeOrderTool(client)

    assistant = AssistantAgent(
        name="shop_assistant",
        llm_config={"config_list": CONFIG_LIST, "tools": [cart_tool, order_tool]},
    )
    return assistant


async def chat(user_message: str) -> AsyncIterable[str]:
    assistant = create_agent()
    user = UserProxyAgent(name="user", code_execution_config={"use_docker": False})
    async for msg in user.initiate_chat(assistant, message=user_message):
        yield msg["content"]
