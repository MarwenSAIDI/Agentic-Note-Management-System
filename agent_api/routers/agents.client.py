import asyncio

from acp_sdk.client import Client
from acp_sdk.models import Message, MessagePart

HOST="127.0.0.1"

async def client() -> None:
    async with Client(base_url=f"http://{HOST}:8080") as client:
        run = await client.run_sync(
            agent="resource-manager",
            input=[
                Message(
                    parts=[MessagePart(content=input('Query: '), content_type="text/plain")]
                )
            ],
        )
        for i, message in enumerate(run.output[0].parts):
            if i > 0 and i < (len(run.output[0].parts) - 1):
                print("AI answer: ", message.content)

if __name__ == "__main__":
    asyncio.run(client())