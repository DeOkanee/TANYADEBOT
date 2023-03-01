import openai
import asyncio
from telebot.async_telebot import AsyncTeleBot

# Masukan API OPENAI & BOT TELEGRAM
openai.api_key = "ISI-DISINI"
bot = AsyncTeleBot('ISI-DISINI')


@bot.message_handler(commands=['start'])
async def send_welcome(message):
    await bot.reply_to(message, """\
Hallo, Saya Google tapi versi duanya, Silakan tanya apa aja....
Waktu DEBOT menjawab akan menyesuaikan dari pertanyaan anda 😃🤔

# /menu
# /about
\
""")

@bot.message_handler(commands=['menu'])
async def send_welcome(message):
    await bot.reply_to(message, """\
Jangan lupa mampir kak ⬇️
"https://blogger.de0ka1.repl.co/"
\
""")

@bot.message_handler(commands=['about'])
async def send_welcome(message):
    await bot.reply_to(message, """\
Ayo manfaatkan aplikasi telegram untuk kepentingan positif,
dan jadikan "TANYADEBOT" sebagai jawaban dari pertanyaanmu"
\
""")
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    response = openai.Completion.create(model="text-davinci-003", prompt=message.text, temperature=0, max_tokens=1000)
    await bot.reply_to(message, response['choices'][0]['text'])


asyncio.run(bot.polling())
