import requests
from bs4 import BeautifulSoup
import aiogram
from aiogram import Bot, Dispatcher, executor, types

api_token = '5496419847:AAHHVX6JS21ktf3iB1E1Jt6xTgmHKqL2-OE'
bot = Bot(token=api_token)
dp = Dispatcher(bot)

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):   
    await message.reply("Hi!, I'm Cryptocurrency Tracker Bot 🤖 ") 
    await message.answer("Enter the name of the cryptocurrency, whose price you want to know 🤑 !!!")

@dp.message_handler()
async def show_crypto(message: types.Message):
    url_lst = (message.text)

    url = 'https://coinmarketcap.com/currencies/' + url_lst + '/'

    full_page = requests.get(url, headers=headers)

    soup = BeautifulSoup(full_page.content, 'html.parser')

    convert = soup.find("div", {"class": "priceValue"})("span")
    convert_num = convert[0].text
    await message.answer(convert_num)

if __name__ == '__main__':
    executor.start_polling(dp)

