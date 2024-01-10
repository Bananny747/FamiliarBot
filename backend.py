import os

# модуль для телеграма
import telebot

# модуль для секретов
from dotenv import load_dotenv

load_dotenv()

# подгружаем секреты
token = os.getenv('TOKEN')

# создаем экземпляр бота с токеном
bot = telebot.TeleBot(token)

# приветственный текст
start_txt = 'Привет! Придумаем что-то классное?'


# обрабатываем старт бота
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, start_txt, parse_mode='Markdown')


def main():
    while True:
        try:
            bot.polling(none_stop=True, interval=0)
        except Exception:
            print('Сработало исключение')


if __name__ == '__main__':
    main()
