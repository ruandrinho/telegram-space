from pathlib import Path
import requests
from urllib.parse import urlsplit, unquote
import os


def download_image(url, filename, params={}):
    Path('images').mkdir(parents=True, exist_ok=True)
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(f'images/{filename}', 'wb') as file:
        file.write(response.content)


def get_extension_from_url(url):
    path = urlsplit(url).path
    path = unquote(path)
    file = os.path.split(path)[1]
    return os.path.splitext(file)[1]