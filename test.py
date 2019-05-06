from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


url = 'https://www.rockauto.com/en/catalog/abarth,1957,750,747cc+l4,1488459,ignition,spark+plug,7212'
browser = webdriver.Chrome(executable_path='./driver/chromedriver')
browser.set_window_size(1200,1200)
browser.get(url)

myElem = WebDriverWait(browser, 4).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'listing-inner')))
for i in myElem:
    soup = BeautifulSoup(str(i.get_attribute('innerHTML')),'lxml')
    manufracturer = soup.findChild('span', class_='listing-final-manufacturer')
    partnumber = soup.findChild('span', class_='listing-final-partnumber')
    de = soup.findChild('span', class_='span-link-underline-remover')
    more_detail = soup.findChild('div', class_='listing-text-row')
    more_detail=more_detail.text+de.text
    price = soup.findChild('span',class_='listing-price')
    print(manufracturer.text,de.text,more_detail,price.text)
    print(partnumber.text)





"""

        csv writer test code
        
"""
import os
import csv

file = os.path.isfile('testcsv.csv')
print(file)

with open('testcsv.csv', 'a', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=',')
    if not file:
        writer.writeheader()

    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

from bs4 import BeautifulSoup
import requests


proxies = {
    "https": "https://103.229.84.141:8080",
    "http": "http://103.229.84.141:8080"
}

source = requests.get('https://www.rockauto.com',proxies=proxies)
print(source.text)