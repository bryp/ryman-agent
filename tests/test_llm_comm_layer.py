from dotenv import load_dotenv, find_dotenv
from ryman_agent.llm import LlmClient, LlmRequest, Message

async def test_llm_comms():
    
    load_dotenv(find_dotenv())

    # create client
    client = LlmClient(model="gemini/gemma-4-31b-it")

    # build request
    request = LlmRequest(
        instructions=["You are a helpful assistant."],
        contents=[Message(role="user", content="What is 2 + 2?")]
    )

    # Generate response
    response = await client.generate(request)

    # Response contains the answer
    for item in response.content:
        if isinstance(item, Message):
            print(item.content)

