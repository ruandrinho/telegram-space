import telegram
import os
from os.path import exists
from dotenv import load_dotenv
from random import choice
import argparse


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description='Загружает изображения запуска SpaceX')
    parser.add_argument('-f', '--file', help='Имя файла')
    args = parser.parse_args()

    if args.file is None:
        args.file = choice(os.listdir('images'))
    if not exists(f'images/{args.file}'):
        print('Неверное имя файла')
        exit()

    bot = telegram.Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
    bot.send_photo(chat_id='@cool_space_photos', photo=open(f'images/{args.file}', 'rb'))


if __name__ == '__main__':
    main()