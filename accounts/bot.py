import logging
import threading
from datetime import datetime
from random import randint

import telebot
from telebot import types

from django.conf import settings

from accounts.models import CustomUser, News
from accounts.utils import get_location, generate_password
from accounts.buttons import new_category_markup, back_menu_markup

from accounts.pars import get_html, proccessing, proccessing_table_2

logging.basicConfig(
    filename='bot_log.log', level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

bot = telebot.TeleBot(settings.TOKENBOT, parse_mode="HTML")

@bot.message_handler(commands=['start'])
def start(message):
    logger = logging.getLogger("Func start")
    logger.info(f"Пользователь {message.chat.id} написал боту start")

    bot_name = bot.get_me().username
    text = (
        f"Добро пожаловать в нашего бота {bot_name}!\n"
        f"Мы рады приветствовать вас в нашем телеграм-боте, где вы можете забронировать место для обучения программированию в ITCBootcamp.\n"
        f"ITCBootcamp - это место, где вы можете расширить свои знания и навыки в области программирования.\n"
        f"Наши курсы позволят вам освоить различные языки программирования, изучить технологии разработки и погрузиться в мир информационных технологий.\n"
        f"Забронируйте место уже сейчас, чтобы начать свой путь к успешной карьере в IT! Просто следуйте инструкциям бота, чтобы зарегистрироваться на наши курсы.\n"
        f"Не упустите возможность стать частью нашего сообщества учеников, которые стремятся к профессиональному росту и достижению своих целей в сфере информационных технологий!\n"
    )
    bot.send_message(message.chat.id, text)

    model_user, created = CustomUser.objects.get_or_create(
        user_id=message.chat.id,
    )

    if created:
        username = message.from_user.username
        if username:
            model_user.username = username.lower()
        else:
            model_user.username = message.from_user.id

        model_user.first_name = message.from_user.first_name if message.from_user.first_name else " "
        model_user.last_name = message.from_user.last_name if message.from_user.last_name else " "
        model_user.user_id = message.from_user.id
        model_user.language_code = message.from_user.language_code
        model_user.is_bot = message.from_user.is_bot

        gen_password = generate_password()
        model_user.password = gen_password

        model_user.set_password(model_user.password)
        model_user.save()

        reg_text = (
            f"Мы вас зарегистрировали, вот ваши данные:\n"
            f"Логин: {model_user.username}\n"
            f"Пароль: {gen_password}"
        )
        bot.send_message(message.chat.id, reg_text, reply_markup=new_category_markup())

    else:
        bot.send_message(message.chat.id, "Вы уже зарегистрированы!", reply_markup=new_category_markup())


@bot.message_handler(func=lambda message: message.text == "Последние")
def last_news(message):
    model_user = CustomUser.objects.get(user_id=message.chat.id)

    if not model_user.DoesNotExist():
        bot.send_message(message.chat.id, "Вы зарегистрированы!")
        return
    
    news_today = News.objects.filter(date=datetime.now().date())
    if not news_today:
        bot.send_message(message.chat.id, "Новостей пока нет!")
        return
    
    for new in news_today:
        text = (
            f"<b>{new.title}</b>\n\n"
            f"{new.info}\n\n"
            f"{new.time} - #DATE{str(new.date).replace('-', '')}"
        )
        bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda message: message.text == "Популярные")
def popular_news(message):
    model_user = CustomUser.objects.get(user_id=message.chat.id)
    
    if not model_user.DoesNotExist():
        bot.send_message(message.chat.id, "Вы не зарегистрированы!")
        return
    
    news_today = News.objects.filter(popular=True, date=datetime.now().date())
    if not news_today:
        bot.send_message(message.chat.id, "Новостей пока нет!")
        return
    
    for new in news_today:
        text = (
            f"<b>{new.title}</b>\n\n"
            f"<tg-spoiler>{new.info}</tg-spoiler>\n\n"
            f"{new.time} - #DATE{str(new.date).replace('-', '')}"
        )
        bot.send_message(message.chat.id, text)

def update_pars_news():
    seconds = float(randint(15, 30) * 60)
    threading.Timer(seconds, update_pars_news).start()
    print(f"Запуск парсинга новостей каждые {seconds} Секунт.")

    html = get_html()
    proccessing_table_2(html)
    proccessing(html)


def RunBot():
    update_pars_news()
    try:
        logger = logging.getLogger("RunBot")
        logger.info("Запуск бота!")
        bot.polling(non_stop=True)

    except KeyboardInterrupt:
        logger.error("Бот остановлен принудительно!")

    except telebot.apihelper.ApiTelegramException:
        pass

    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}!")


