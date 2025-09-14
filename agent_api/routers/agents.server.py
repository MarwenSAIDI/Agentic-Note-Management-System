import asyncio
from acp_sdk import MessagePart
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

from langchain_ollama.chat_models import ChatOllama
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
import asyncio
from collections.abc import AsyncGenerator

from acp_sdk.models import Message
from acp_sdk.server import Context, RunYield, RunYieldResume, Server

HOST="127.0.0.1"
PORT=8080

model = ChatOllama(model="qwen2.5:3b")
server = Server()

@server.agent(name="resource-manager")
async def resource_manager(
    input: list[Message], context: Context
) -> AsyncGenerator[RunYield, RunYieldResume]:
    """This agent handles request regqrding managing resources provided
     by the user like URLs and PDFs and returning them as text format to be used later.
    """
    # Connect using the new streamable-http client helper
    async with streamablehttp_client(f"http://{HOST}:8001/mcp") as (read, write, get_session_id):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # Call tools
            tools = await load_mcp_tools(session)

            agent = create_react_agent(model, tools)

            response = await agent.ainvoke({"messages": input[0].parts[0].content})
            
            message_parts_list = [MessagePart(content=str(message.content) , content_type='text/plain') for message in response['messages']]

            yield Message(
                parts=message_parts_list
            )


if __name__ == "__main__":
    server.run(
        host=HOST,
        port=PORT,
    )