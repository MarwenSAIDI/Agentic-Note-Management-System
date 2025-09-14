from typing import Dict
import requests
import PyPDF2
from langchain_community.document_loaders import YoutubeLoader
from youtube_transcript_api import YouTubeTranscriptApi
from mcp.server import FastMCP

from schemas.output_text import OutputText
from schemas.output_type_enum import OutputTypeEnum


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

@server.tool(name="Get the text from web page URL")
async def get_text_from_web_url(
    url: str,
    title: str
) -> OutputText:
    """This tool allow us to return the body of a web page URL in a text format.

    Args:
        url (str): the URL we want to parse
        title (str): the title of the web page

    Returns:
        str: the body in a text format
    """

    body = requests.get(url).text

    return OutputText(type=OutputTypeEnum.WEB_PAGE, content=body, title=title, source=url)

@server.tool(name="Get Youtube video transcript from URL")
async def get_youtube_video_transcript(
    url_video:str,
    title:str,
) -> OutputText:
    """This tools takes a Youtube video URL and extracts the transcription of the video into text.

    Args:
        url_video (str): A Youtube video URL
        title (str): the title of the web page

    Returns:
        str: The transcription of the video
    """

    video_id = YoutubeLoader.extract_video_id(url_video)
    ytt_api = YouTubeTranscriptApi()

    # retrieve the available transcripts
    transcript_list = ytt_api.list(video_id)

    transcript = [transcript.fetch() for transcript in transcript_list]

    texts = [snippet.text for snippet in transcript[0].snippets]


    # # translating the transcript will return another transcript object
    # print(transcript.translate('en').fetch())

    # # you can also directly filter for the language you are looking for, using the transcript list
    # transcript = transcript_list.find_transcript(['de', 'en'])

    # # or just filter for manually created transcripts
    # transcript = transcript_list.find_manually_created_transcript(['de', 'en'])

    # # or automatically generated ones
    # transcript = transcript_list.find_generated_transcript(['de', 'en'])

    return OutputText(type=OutputTypeEnum.YOUTUBE_VIDEO, content=str('\n\n'.join(texts)), title=title, source=url_video)

@server.tool(name="Get text from a PDF file")
async def get_text_from_pdf(
    file_content_path: str,
    title: str
) -> OutputText:
    """This tool loads a PDF file using the path, opens' it, and return the content to text format.

    Args:
        file_content_path (str): The PDF file path
        title (str): the title of the web page

    Returns:
        str: The extracted text
    """
    with open(file_content_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)

        texts = [page.extract_text() for page in reader.pages]

    return OutputText(type=OutputTypeEnum.PDF_FILE, content=str('\n'.join(texts)), title=title)

if __name__ == '__main__':
    server.run(transport='stdio')