import telegram
import os
from dotenv import load_dotenv
from random import shuffle
import time


def main():
    load_dotenv()
    interval = int(os.getenv('AUTO_PUBLICATION_INTERVAL', default=240))
    bot = telegram.Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
    while True:
        for root, dirs, files in os.walk('images'):
            shuffle(files)
            for file in files:
                with open(f'images/{file}', 'rb') as image:
                    bot.send_photo(chat_id='@cool_space_photos', photo=image)
                time.sleep(interval*60)


if __name__ == '__main__':
    main()