import requests
import bs4 

import tk 

def get_html_data(url):
    response = requests.get(url)
    return response.text

def get_covid_data():
    url = 'https://www.worldometers.info/coronavirus/'
    html_data = get_html_data(url)
    soup = bs4.BeautifulSoup(html_data, 'html.parser')
    print (soup.prettify())
    info_div = bs.find('div', class_='content_inner').findAll('div', class_='maincounter-number')
    all_data = []
    for block in info_div:
        text = block.find("h1", class_= None).get_text()
        count = block.find("span", class_= None).get_text()
        all_data = all_data + text + " " + count + "\n"

    print(all_data)

get_covid_data()