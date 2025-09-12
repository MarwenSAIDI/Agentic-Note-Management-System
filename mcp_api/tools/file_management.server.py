from typing import Dict
import requests
from mcp.server import FastMCP


server = FastMCP(
    name="File management tools",
    host='127.0.0.1',
    port=8001
)

@server.tool(name='Health Check')
async def health_check() -> Dict[str,int]:
    """ The healthcheck function check if the following server 
    is active by return a dictionnary that has a status code 200.

    Returns:
        Dict[str,int]: the dictinnary of the 'status' code 200
    """
    return {'status': 200}

@server.tool(name="Get the text from URL")
async def get_text_from_url(url: str) -> str:
    """This tool allow us to return the body of an URL in a text format.

    Args:
        url (str): the URL we want to parse

    Returns:
        str: the body in a text format
    """

    body = requests.get(url).text

    return body

if __name__ == '__main__':
    server.run(transport='stdio')