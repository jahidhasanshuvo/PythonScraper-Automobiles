import os
import csv

# file = os.path.isfile('testcsv.csv')
# print(file)
#
# with open('testcsv.csv', 'a', newline='') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=',')
#     if not file:
#         writer.writeheader()
#
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

from bs4 import BeautifulSoup
import requests


proxies = {
    "https": "168.228.192.13:49992",
    "http": "168.228.192.13:49992"
}

source = requests.get('https://www.rockauto.com/',proxies=proxies)
print(source.text)


#
# domain = 'https://www.rockauto.com/en/catalog/abarth,1969,1000,982cc+l4,1438885,brake+&+wheel+hub'
# brand_source = requests.get(domain).text
# brand_soup = BeautifulSoup(brand_source,'lxml')
# brands = brand_soup.find_all('a',class_='navlabellink nvoffset nimportant')
# print(len(brands))
# for brand in brands:
#     print(brand['href'])