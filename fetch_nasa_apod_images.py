import requests
import datetime
import argparse
import os
from file_utils import download_image, get_file_extension
from dotenv import load_dotenv


def fetch_nasa_apod_images(days=1):
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


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description='Загружает изображения NASA APOD')
    parser.add_argument('-d', '--days', type=int, help='Количество дней', default=1)
    args = parser.parse_args()
    fetch_nasa_apod_images(args.days)



if __name__ == '__main__':
    main()