import requests
import datetime
import fake_useragent
import telebot
import pprint
import aiofiles
import random
import time
import pprint
import urllib
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from bs4 import BeautifulSoup as b
import pyrogram
import asyncio
import types
import time
import pprint
from pyrogram import Client






user = fake_useragent.UserAgent().random
header = {'user-agent': user}

link = 'https://news.ru/'


bot_token = '5906415662:AAF-bx-444pANJ0KYwyL5za0trJJTHw3oQY'

bot = Bot(token=bot_token)
dp = Dispatcher(bot)

api_id = 23673413
api_hash = "16925f557b1491818d8633e3a26191ad"

i = 'novosti44444'

app = Client(
    "my_account",
    api_id=api_id, api_hash=api_hash
    # bot_token=bot_token
)
spisklink = []
spisklink1 = []
finalspi = []





async def main():

    while True:
        r = requests.get(f'{link}', headers=header)
        soup = b(r.text, 'html.parser')
        divimport = soup.find_all('div', class_='center-importanrt__item')

        for lg in divimport:
            linkimport = lg.find('a').get('href')
            linkf = 'https://news.ru/'+linkimport
            spisklink.append(linkf)
        

        
        with open(file='xxx.txt', mode='r', encoding='UTF-8') as bbb:
            contents = bbb.readlines()
            for j in contents:
                
                # spisklink1.append(j)
                spisklink1.append(j.replace('\n', ''))
            bbb.close()
        
    
        # print(spisklink1[5])
        print(len(spisklink1))
        

    
        for g in spisklink:
            if g in spisklink1:
                print(g in spisklink1)
                continue
            else:
                print(g in spisklink1)
                
                r1 = requests.get(f'{g}', headers=header)
                soup1 = b(r1.text, 'html.parser')

                title1 = soup1.find('div', class_='single-news__title')
                title2 = title1.find('h1').text

                pic1= soup1.find('div', class_='single-news__image')
                pic2 = pic1.find('link').get('href')

                desc = soup1.find('div', class_='bottom-news__txt-normal annotation').text


                with open(file='xxx.txt', mode='a', encoding='UTF-8') as mmm:
                    mmm.write(g)
                    mmm.write('\n')
                    mmm.close()

                async with app:
                    await app.send_message(i, f'{title2}\n{pic2}\n{desc}')
        time.sleep(10)
            

app.run(main())
    
    #     a = g in spisklink1

    #     if a == True:
    #         try:
    #             print('ссылки есть в скиске')
    #             continue

    #         except:
    #             
    #             r1 = requests.get(f'{g}', headers=header)
    #             soup1 = b(r1.text, 'html.parser')

    #             title1 = soup1.find('div', class_='single-news__title')
    #             title2 = title1.find('h1').text

    #             pic1= soup1.find('div', class_='single-news__image')
    #             pic2 = pic1.find('link').get('href')

    #             desc = soup1.find('div', class_='bottom-news__txt-normal annotation').text

    #             async with app:
    #                 await app.send_message(i, f'{title2}\n{pic2}\n{desc}')
    #             time.sleep(1.12)


        
        # # with open('xxx.txt', mode='a', encoding='UTF-8') as file:
        # #         file.write(g)
        # #         file.write('\n')
        # #         file.close()
       
        # if g in spisklink1 == True:
        #     continue
          
        # else:
        #     with open('xxx.txt', mode='a', encoding='UTF-8') as file:
        #         file.write(g)
        #         file.write('\n')
        #         file.close()
        
        # if g in spisklink1 == True:
            # try:
            #     print('ссылки есть в скиске')
            #     continue

            # except:
            #     print(g in spisklink1)
            #     r1 = requests.get(f'{g}', headers=header)
            #     soup1 = b(r1.text, 'html.parser')

            #     title1 = soup1.find('div', class_='single-news__title')
            #     title2 = title1.find('h1').text

            #     pic1= soup1.find('div', class_='single-news__image')
            #     pic2 = pic1.find('link').get('href')

            #     desc = soup1.find('div', class_='bottom-news__txt-normal annotation').text

            #     async with app:
            #         await app.send_message(i, f'{title2}\n{pic2}\n{desc}')
            #     time.sleep(1.12)
        
            

   
    
    
    
    
    





    # r1 = requests.get(f'{spisklink[0]}', headers=header)
    # soup1 = b(r1.text, 'html.parser')

    # title1 = soup1.find('div', class_='single-news__title')
    # title2 = title1.find('h1').text

    # pic1= soup1.find('div', class_='single-news__image')
    # pic2 = pic1.find('link').get('href')

    # desc = soup1.find('div', class_='bottom-news__txt-normal annotation').text

    


    # async with app:
    #     await app.send_message(i, f'{title2}\n{pic2}\n{desc}')
        
    
    
    


    
# if __name__ == '__main__':
#     main()



    


# async def main():
   
#     r = requests.get(f'{link}', headers=header)
#     soup = b(r.text, 'html.parser')
#     divimport = soup.find_all('div', class_='center-importanrt__item')

#     for lg in divimport:
#         linkimport = lg.find('a').get('href')
#         linkf = 'https://news.ru/'+linkimport
#         spisklink.append(linkf)

#     for i in spisklink:
#         async with aiofiles.open('xxx.txt', mode='w', encoding='UTF-8') as file:
#             await file.write(i)
#             await file.close()
    

# asyncio.run(main())


    # for g in spisklink:
    #     if g in spisklink1 == True:
    #         print(g in spisklink1)
    #         print('совпадения найдены')
    #         continue
    #     else:
    #         print(g in spisklink1)
    #         r1 = requests.get(f'{g}', headers=header)
    #         soup1 = b(r1.text, 'html.parser')

    #         title1 = soup1.find('div', class_='single-news__title')
    #         title2 = title1.find('h1').text

    #         pic1= soup1.find('div', class_='single-news__image')
    #         pic2 = pic1.find('link').get('href')

    #         desc = soup1.find('div', class_='bottom-news__txt-normal annotation').text
    #         # async with app:
    #         #     await app.send_message(i, f'{title2}\n{pic2}\n{desc}')
    #         time.sleep(3.1)
    #         with open('xxx.txt', mode='a', encoding='UTF-8') as bbb:
    #             bbb.write(g)
    #             bbb.write('\n')
    #             bbb.close()
    
