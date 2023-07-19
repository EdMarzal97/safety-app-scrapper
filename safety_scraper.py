"""a scraper for get the data from countries"""
import csv
import requests
from bs4 import BeautifulSoup

URL_BASE = 'https://www.travelsafe-abroad.com/'

result = requests.get(URL_BASE, timeout=1000)
content = result.text
soup = BeautifulSoup(content, 'lxml')

data = []
country_list= soup.find_all('h2')
for country in country_list:
    country_title = country.get_text()
    country_result = requests.get(url=f'https://www.travelsafe-abroad.com/{country_title}',timeout=10)
    country_content = country_result.text
    country_soup = BeautifulSoup(country_content, 'lxml')
    country_rate = country_soup.find('span',id='percent')
    rate = country_rate.text
    country_overall_risk = country_soup.find('h3', id='overall-risk')
    overall_risk = country_overall_risk.text
    country_transport_risk = country_soup.find('h3', id='transport-and-taxis-risk')
    transport_risk = country_transport_risk.text
    country_pickpocket_risk = country_soup.find('h3', id='pickpockets-risk')
    pickpocket_risk = country_pickpocket_risk.text
    country_natural_risk = country_soup.find('h3', id='natural-disasters-risk')
    natural_risk = country_natural_risk.text
    country_mugging_risk = country_soup.find('h3', id='mugging-risk')
    mugging_risk = country_mugging_risk.text
    country_terrorism_risk = country_soup.find('h3', id='terrorism-risk')
    terrorism_risk = country_terrorism_risk.text
    country_scam_risk = country_soup.find('h3', id='scams-risk')
    scam_risk = country_scam_risk.text
    country_women_risk = country_soup.find('h3', id='women-travelers-risk')
    women_risk = country_women_risk.text
    information = {
        'title': country_title,
        'rate': rate,
        'overall': overall_risk,
        'transport_risk': transport_risk,
        'pickpocket_risk': pickpocket_risk,
        'natural_risk': natural_risk,
        'mugging_risk': mugging_risk,
        'terrorism_risk': terrorism_risk,
        'scam_risk': scam_risk,
        'women_risk': women_risk
    }
    data.append(information)
    


csv_columns = [ 'title','rate','overall','transport_risk','pickpocket_risk','natural_risk','mugging_risk','terrorism_risk','scam_risk','women_risk']

csv_file = 'country_data.csv'

try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for info in data:
            writer.writerow(info)
except IOError:
    print("I/O error")
    