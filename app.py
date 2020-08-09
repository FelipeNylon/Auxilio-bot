from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from random import *
import os
import time 
from var import *


class TwitterBot: 
    def __init__(self,username, password,twitti):
        self.username = username
        self.password = password
        self.twitti = twitti
        self.bot = webdriver.Chrome()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(4)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        twitti = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        twitti.send_keys(self.twitti)
      


        time.sleep(4)


parcela = randint(1, 10000)
dia = randint(1,31)
mes = randint(1,12)
ano = randint(2020,2700)

if dia<10:
    dia = "0{}".format(dia)    


if mes<10:
    mes = "0{}".format(mes)   

#atenção eu usei variáveis de ambiente no nome de usuário e senha da conta do bot, você pode usar variáveis de ambiente ou string mesmo 
auxilio = TwitterBot(os.environ["USER"], os.environ["USER_PASSWORD"], 'o pagamento da {}º parcela do auxilio emergencial começa no dia {}/{}/{} '.format(parcela,dia,mes,ano))
auxilio.login()
