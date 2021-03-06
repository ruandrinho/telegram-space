import requests
import datetime
import argparse
import os
from file_utils import download_image
from dotenv import load_dotenv


def fetch_nasa_epic_images(api_key, count=1):
    url = 'https://api.nasa.gov/EPIC/api/natural'
    response = requests.get(url, params={'api_key': api_key})
    for n, item in enumerate(response.json()[:count]):
        img_datetime = datetime.datetime.fromisoformat(item['date'])
        img_url = 'https://api.nasa.gov/EPIC/archive/natural/'
        img_url += f'{img_datetime.year}/{img_datetime.month:02d}/'
        img_url += f'{img_datetime.day:02d}/png/{item["image"]}.png'
        download_image(
            img_url,
            f'nasa_epic_{n:02d}.png',
            {'api_key': api_key}
        )


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(
        description='Загружает изображения NASA EPIC'
    )
    parser.add_argument('-c', '--count', type=int, help='Количество',
                        default=1)
    args = parser.parse_args()
    fetch_nasa_epic_images(os.getenv('NASA_API_KEY'), args.count)


if __name__ == '__main__':
    main()
