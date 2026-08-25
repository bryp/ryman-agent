# tests/test_agent.py
from ryman_agent import __version__  
from ryman_agent.agent import Agent
from ryman_agent.llm import LlmClient
from ryman_agent.tools.calculator import calculator
from ryman_agent.tools.search import search_web
from ryman_agent.tools.base import FunctionTool
from ryman_agent.utils import display_trace

import pytest


async def test_agent():

    agent = Agent(
        model=LlmClient(model="gemini/gemma-4-31b-it"),
        tools=[FunctionTool(calculator), FunctionTool(search_web)],
        instructions="You are a helpful assistant"
    )

    result = await agent.run("What is 1234 * 5678?")

    print(result.output)
    display_trace(result.context)