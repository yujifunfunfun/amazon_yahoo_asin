
import requests
from bs4 import BeautifulSoup
import re
import csv

def save_csv(data):
    with open('csv/yahoo_keyword_ranking_bs.csv','a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow([data])

def fetch_yahoo_keyword_bs():
    url = 'https://climb-factory.co.jp/tool/YahooShoppingTool/YahooKeywordRanking.php'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    elems = soup.find_all('td')
    print(len(elems))

    keyword_list = []
    for elem in elems:
        p = r'>(.*)<'  
        keyword = re.search(p, str(elem)).group(1)
        keyword_list.append(keyword)
    keyword_list = list(set(keyword_list))
    for keyword in keyword_list:
        save_csv(keyword)

if __name__ == "__main__":
    fetch_yahoo_keyword_bs()

