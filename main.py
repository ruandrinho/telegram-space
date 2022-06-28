import requests
from pathlib import Path
from urllib.parse import urlsplit, unquote
import datetime
import os
from dotenv import load_dotenv


def download_image(url, filename, params={}):
    Path('images').mkdir(parents=True, exist_ok=True)
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(f'images/{filename}', 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v5/launches/latest'
    response = requests.get(url)
    response.raise_for_status()
    for n, img in enumerate(response.json()['links']['flickr']['original']):
        download_image(img, f'spacex{n:02d}.jpg')


def fetch_nasa_apod(days=1):
    load_dotenv()
    url = 'https://api.nasa.gov/planetary/apod'
    today = datetime.date.today()
    response = requests.get(url, params={
        'api_key': os.getenv('NASA_API_KEY'),
        'end_date': today,
        'start_date': today - datetime.timedelta(days=days-1)
    })
    for n, item in enumerate(response.json()):
        if item['media_type'] != 'image':
            continue
        extension = get_file_extension(item['hdurl'])
        download_image(item['hdurl'], f'nasa_apod_{item["date"]}{extension}')


def fetch_nasa_epic(num=1):
    load_dotenv()
    url = 'https://api.nasa.gov/EPIC/api/natural'
    response = requests.get(url, params={
        'api_key': os.getenv('NASA_API_KEY')
    })
    for n, item in enumerate(response.json()[:num]):
        img_datetime = datetime.datetime.fromisoformat(item['date'])
        img_url = f'https://api.nasa.gov/EPIC/archive/natural/{img_datetime.year}/{img_datetime.month:02d}/{img_datetime.day:02d}/png/{item["image"]}.png'
        download_image(
            img_url, 
            f'nasa_epic_{n:02d}.png', 
            {'api_key': os.getenv('NASA_API_KEY')}
        )


def get_file_extension(url):
    path = urlsplit(url).path
    path = unquote(path)
    file = os.path.split(path)[1]
    return os.path.splitext(file)[1]
    

if __name__ == '__main__':
    fetch_nasa_epic()