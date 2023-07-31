import telebot
from telebot import types

bot = telebot.TeleBot("6433719050:AAE6tnR7jOSBza4uelfvAW5JTYmQW-GiAk8")

print('_____ START BOT _____')

def simple_numbers(star_value, end_value):
    simple_num = []
    for i in range(star_value, end_value):
        flag = True
        for dil in range(star_value, end_value):
            if dil != 1 and dil < i:
                result = i % dil
                if result == 0:
                    flag = False
                    break
            if dil >= i:
                break
        if flag:
            simple_num.append(i)
    return simple_num

def main_reply_menu():

    # ---Перший варіант створення кнопок (не дуже топ)
    # markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    # itembtn1 = types.KeyboardButton('🏛️a')
    # itembtn2 = types.KeyboardButton('🌎v')
    # itembtn3 = types.KeyboardButton('/start')
    # markup.add(itembtn1, itembtn2, itembtn3)

    # ---Другий варіант створення кнопок (топ)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(types.KeyboardButton('⚡Btn 1'), types.KeyboardButton('💧Btn 2'), types.KeyboardButton('🔥Btn 3'))
    markup.row(types.KeyboardButton('Прості числа'))
    markup.row(types.KeyboardButton('/start'), types.KeyboardButton('/update'))
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(msg):
    cid = msg.chat.id
    bot.send_message(cid, "Hello!", reply_markup=main_reply_menu())
	# bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['update'])
def some_msg(msg):
    bot.reply_to(msg, "Update✅", reply_markup=main_reply_menu())

@bot.message_handler(func=lambda message: True)
def echo_all(msg):
	# bot.reply_to(message, message.text)

    if msg.text == 'Прості числа':
        cid = msg.chat.id
        numbers = simple_numbers(1, 100)
        temp_text = 'Список простих чисел: \n\n'
        for num in numbers:
            temp_text += f"{num} "
        bot.send_message(cid, temp_text)

bot.infinity_polling()