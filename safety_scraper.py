"""a scraper for get the data from countries"""
import csv
import requests
from bs4 import BeautifulSoup

URL_BASE = 'https://www.travelsafe-abroad.com/'

result = requests.get(URL_BASE, timeout=1000)
content = result.text
soup = BeautifulSoup(content, 'lxml')

data = []
country_list= soup.find_all('h2', limit=2)
for country in country_list:
    country_title = country.get_text()
    country_result = requests.get(url=f'https://www.travelsafe-abroad.com/{country_title}',timeout=10)
    country_content = country_result.text
    country_soup = BeautifulSoup(country_content, 'lxml')
    country_rate = country_soup.find('span',id='percent')
    rate = country_rate.text
    country_overall_risk = country_soup.find('h3', id='overall-risk').find('span')
    overall_risk = country_overall_risk.text
    country_transport_risk = country_soup.find('h3', id='transport-and-taxis-risk').find('span')
    transport_risk = country_transport_risk.text
    country_pickpocket_risk = country_soup.find('h3', id='pickpockets-risk').find('span')
    pickpocket_risk = country_pickpocket_risk.text
    country_natural_risk = country_soup.find('h3', id='natural-disasters-risk').find('span')
    natural_risk = country_natural_risk.text
    country_mugging_risk = country_soup.find('h3', id='mugging-risk').find('span')
    mugging_risk = country_mugging_risk.text
    country_terrorism_risk = country_soup.find('h3', id='terrorism-risk').find('span')
    terrorism_risk = country_terrorism_risk.text
    country_scam_risk = country_soup.find('h3', id='scams-risk').find('span')
    scam_risk = country_scam_risk.text
    country_women_risk = country_soup.find('h3', id='women-travelers-risk').find('span')
    women_risk = country_women_risk.text
    information = {
        'name': country_title,
        'rate': rate,
        'overall': overall_risk,
        'transport': transport_risk,
        'pickpockets': pickpocket_risk,
        'natural': natural_risk,
        'mugging': mugging_risk,
        'terrorism': terrorism_risk,
        'scams': scam_risk,
        'women': women_risk
    }
    data.append(information)
    
    
csv_columns = [ 'name','rate','overall','transport','pickpockets','natural','mugging','terrorism','scams','women']

csv_file = 'country_data.csv'

try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for info in data:
            writer.writerow(info)
except IOError:
    print("I/O error")