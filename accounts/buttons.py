from telebot import types


def new_category_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    b1 = types.KeyboardButton('Последние')
    b2 = types.KeyboardButton('Популярные')

    return markup.add(b1, b2)


def back_menu_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    b1 = types.KeyboardButton('Меню')

    return markup.add(b1)
