import requests
from bs4 import BeautifulSoup
#import aiogram
#from aiogram import Bot, Dispatcher, executor, types

def currency():

    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
    url_list = []
    
    num = 5
    while len(url_list) != 5:
        url_list.append(input("Введите " + str(num) + " криптовалют: \n"))
        num -= 1
    print(url_list)

    list_num = 0
    while list_num != 5:
        url = 'https://coinmarketcap.com/currencies/' + url_list[list_num] + '/'

        full_page = requests.get(url, headers=headers)

        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.find("div", {"class": "priceValue"})("span")
        convert_num = convert[0].text
        print(convert_num)
        list_num += 1
currency()
