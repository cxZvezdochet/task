
# bot = telebot.TeleBot("6222492056:AAEjkTwhOGS7aYy04vIRXwBIic5WtUNYanc"
import telebot
from telebot import types


bot = telebot.TeleBot("6222492056:AAEjkTwhOGS7aYy04vIRXwBIic5WtUNYanc")

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text='Выбери меню', callback_data='menu')
    keyboard.add(button)
    bot.send_message(message.chat.id, 'Привет, Данилий! Нажми на кнопку, чтобы открыть меню:', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'menu':
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='Расписание', callback_data='button1')
        button2 = types.InlineKeyboardButton(text='Добавить Дз', callback_data='button2')
        keyboard.add(button1, button2)
        bot.send_message(call.message.chat.id, 'Выбери раздел:', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'button1':
        bot.send_message(chat_id=call.message.chat.id, text='Введите текст или прикрепите файл:')
        # Здесь вы можете обработать введенный текст или прикрепленный файл

# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     # Создаем клавиатуру с кнопками
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     itembtn1 = types.KeyboardButton('Расписание')
#     itembtn2 = types.KeyboardButton('Добавить дз')
#     Ponedelnik = types.KeyboardButton('Понедельник')
#     Vtornik = types.KeyboardButton('Вторник')
#     Sreda = types.KeyboardButton('Среда')
#     Chetverg = types.KeyboardButton('Четверг')
#     Pyatnica = types.KeyboardButton('Пятница')
#     Subbota = types.KeyboardButton('Суббота')
#     keyboard.row(itembtn1, itembtn2)
#
#     @bot.message_handler(func=lambda message: True)
#     def echo_all(message):
#         # Проверяем, какую кнопку нажал пользователь
#         if message.text == 'Расписание':
#             call.data = "Расписание"
#         elif message.text == 'Добавить дз':
#             bot.reply_to(message, 'Сюда написать код с дз')
#
#     @bot.callback_query_handler(func=lambda call: True)
#     def callback_handler(call):
#         if call.data == 'Расписание':
#             keyboard = types.InlineKeyboardMarkup()
#             button1 = types.InlineKeyboardButton(text='Понедельник', callback_data='Расписание')
#             button2 = types.InlineKeyboardButton(text='Вторник', callback_data='Расписание')
#             button3 = types.InlineKeyboardButton(text='Выбери файл или скинь текст', callback_data='button3')
#             keyboard.add(button1, button2, button3)
#             bot.send_message(call.message.chat.id, 'Выбери кнопку:', reply_markup=keyboard)
#
#
#     @bot.message_handler(commands=['sizeKeyboard'])
#     def start(message):
#         bot.send_message(message.chat.id, 'Привет, Данилий! Выбери кнопку:', reply_markup=keyboard)
#         # Отправляем приветственное сообщение с клавиатурой
#     bot.reply_to(message, "Привет.", reply_markup=keyboard)







    # name = message.from_user.first_name
    # usid = message.from_user.id
    # bot.send_message(message.from_user.id, name + ' ты думал здесь что-то будет?')
    # bot.send_photo(message.from_user.id,
    #                'https://sun9-21.userapi.com/impg/TUiDADp0rUZk3uUochh9ZXecG5Fu0EVmi6-EkQ/e47UuVT6fDo.jpg?size=600x533&quality=96&sign=46e7064407ed89fe37b5ea372b897c1b&type=album')

    # bot.send_message(message.from_user.id, 'Твой id: ' + str(usid))
    # bot.send_message(5766665003, 'Боту прислали сообщение: <' + message.text + '> \nid пользователя: <' + str(
    #     usid) + '> \nИмя пользователя: <' + name + '>')


bot.infinity_polling(timeout=(15), long_polling_timeout=5)