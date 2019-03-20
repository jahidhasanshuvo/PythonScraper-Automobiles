from bs4 import BeautifulSoup
import requests
import csv,os

file = os.path.isfile('rockauto.csv')

proxies = {
    "https": "103.112.128.6:53281",
    "http": "103.112.128.6:53281"
}

# source = requests.get('https://www.rockauto.com/',proxies=proxies)
# print(source.text)
domain = 'https://www.rockauto.com'

def requestUsingProxies(url):
    return requests.get(url).text

def findAnchor(input):
    if input is None:
        url = domain
    else:
        url = domain+input['href']
    source = requestUsingProxies(url)
    soup = BeautifulSoup(source, 'lxml')
    output = soup.findChildren('a', class_='navlabellink nvoffset nnormal')
    return output


with open('rockauto.csv', 'a', newline='') as csvfile:
    fieldnames = ['Brand', 'Year','Model','Engine','Category','SubCategory','Manufacturer','PartNumber','MoreDetails','Price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')
    if not file:
        writer.writeheader()

    brands = findAnchor(None)
    for brand in brands:
        years=findAnchor(brand)
        for year in years[1:]:
            # print(year.text)
            models=findAnchor(year)
            for model in models[2:]:
                engines=findAnchor(model)
                for engine in engines[3:]:
                    categories = findAnchor(engine)
                    for category in categories[4:]:
                        sub_category_source = requestUsingProxies(domain + category['href'])
                        sub_category_soup = BeautifulSoup(sub_category_source, 'lxml')
                        sub_categories = sub_category_soup.findChildren('a', class_='navlabellink nvoffset nimportant')
                        if len(sub_categories) == 0:
                            sub_categories = sub_category_soup.findChildren('a', class_='navlabellink nvoffset nnormal')
                            sub_categories=sub_categories[5:]

                        for sub_category in sub_categories:
                            details_source = requestUsingProxies(domain + sub_category['href'])
                            details_soup = BeautifulSoup(details_source, 'lxml')

                            details = details_soup.findChildren('tbody',class_='listing-inner')
                            for detail in details:
                                product_id=detail['id'].split('[')
                                product_id=product_id[1].split(']')
                                product_id = product_id[0]

                                detail_soup = BeautifulSoup(str(detail),'lxml')
                                manufracturer = detail_soup.findChild('span',class_='listing-final-manufacturer')
                                partnumber = detail_soup.findChild('span',class_='listing-final-partnumber')
                                more_detail = detail_soup.findChild('span',class_='span-link-underline-remover')
                                if more_detail is None:
                                    more_detail='N/A'
                                else:
                                    more_detail=more_detail.text
                                price = details_soup.findChild('span',id= 'dprice['+product_id+'][v]')
                                print(f'{brand.text}--,{year.text},'
                                      f'--{model.text}--{engine.text}--{category.text}--{sub_category.text}-'
                                      f'-{manufracturer.text}--{partnumber.text}-{more_detail}-{price.text}')

                                writer.writerow({'Brand': brand.text, 'Year':year.text, 'Model':model.text, 'Engine':engine.text,
                                        'Category':category.text, 'SubCategory':sub_category.text, 'Manufacturer':manufracturer.text,
                                        'PartNumber':partnumber.text, 'MoreDetails':more_detail, 'Price':price.text})
