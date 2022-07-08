from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import time
import urllib

import pandas as pd

#import contacts from xlsx file
contacts = pd.read_excel("contatos.xlsx")

desired_cap = {
}

#create a new broswer
#browser = webdriver.Edge(executable_path='/Users/renand.pbarbono/Desktop/CEAD/WAmessageSender/msedgedriver',capabilities=desired_cap)
browser  = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://web.whatsapp.com/")

while len(browser.find_elements_by_id('side')) < 1:
    time.sleep(1)
    print("Esperando Whatsapp web carregar...")

#send message to each contact
for i, phone in enumerate(contacts['Mobile Phone']):
    FirstName = contacts['First Name'][i]
    LastName = contacts['Last Name'][i]
    msg = "Olá, " + FirstName.title() + " " + LastName.title() + "!\n\n Para qualquer dúvida em relação a sua matrícula entre em contato com a gente pelo https://wa.me/553584796918"
    text = urllib.parse.quote(msg)
    link = f"https://web.whatsapp.com/send?phone=+55{phone}&text={text}" 
    browser.get(link)
    while len(browser.find_element_by_id("side")) < 1:
        time.sleep(30)
        browser.find_element_by_id_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span').send_keys(Keys.ENTER)
        time.sleep(30)


         