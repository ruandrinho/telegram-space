import telegram
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    bot = telegram.Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
    bot.send_photo(chat_id='@cool_space_photos', photo=open('images/nasa_epic_00.png', 'rb'))


if __name__ == '__main__':
    main()