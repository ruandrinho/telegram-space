import requests
import argparse
from file_utils import download_image


def main(launch_id='latest'):
    parser = argparse.ArgumentParser(description='Загружает изображения запуска SpaceX')
    parser.add_argument('--id', help='ID запуска', default='latest')
    args = parser.parse_args()

    url = f'https://api.spacexdata.com/v5/launches/{args.id}'
    response = requests.get(url)
    response.raise_for_status()
    for n, img in enumerate(response.json()['links']['flickr']['original']):
        download_image(img, f'spacex_{n:02d}.jpg')


if __name__ == '__main__':
    main()