import requests

def read_url(url: str) -> str:
    return requests.get(url).text