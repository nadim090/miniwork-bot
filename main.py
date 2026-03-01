import telebot
from telebot import types

API_TOKEN = '8669637001:AAG85sWw9y7JkR85fh0Hp8I8RQGcUfFBeXc'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    item1 = types.KeyboardButton("💰 Investment Plans")
    item2 = types.KeyboardButton("👤 My Profile")
    item3 = types.KeyboardButton("💳 Deposit")
    item4 = types.KeyboardButton("🏦 Withdraw")
    markup.add(item1, item2, item3, item4)
    
    bot.send_message(message.chat.id, 
                     f"স্বাগতম {message.from_user.first_name}!\n@Miniworkpro_bot এ আপনাকে স্বাগতম।", 
                     reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "💰 Investment Plans")
def show_plans(message):
    plans = ("আমাদের প্ল্যানসমূহ:\n\n"
             "১. সিলভার: ১০০ টাকা (দৈনিক ৫ টাকা)\n"
             "২. গোল্ড: ৫০০ টাকা (দৈনিক ৩০ টাকা)")
    bot.send_message(message.chat.id, plans)

@bot.message_handler(func=lambda message: message.text == "👤 My Profile")
def my_profile(message):
    info = f"👤 নাম: {message.from_user.first_name}\n💰 ব্যালেন্স: 0.00 BDT"
    bot.send_message(message.chat.id, info)

@bot.message_handler(func=lambda message: message.text == "💳 Deposit")
def deposit(message):
    bot.send_message(message.chat.id, "টাকা জমা দিতে অ্যাডমিনকে নক দিন।")

@bot.message_handler(func=lambda message: message.text == "🏦 Withdraw")
def withdraw(message):
    bot.send_message(message.chat.id, "আপনার ব্যালেন্স পর্যাপ্ত নয়।")

bot.infinity_polling()
