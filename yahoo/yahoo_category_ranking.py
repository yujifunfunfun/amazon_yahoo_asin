import csv
import sys
import math
import requests
import urllib.parse
import os
from os.path import join, dirname
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from dotenv import load_dotenv
from logger import set_logger
import urllib.parse
import math

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

logger = set_logger(__name__)


yahoo_app_id = os.environ.get("YAHOO_APP_ID")


def save_csv(data):
    with open('csv/yahoo_category_ranking.csv','a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow([data])

def fetch_yahoo_keyword():
    request_url = f'https://shopping.yahooapis.jp/ShoppingWebService/V2/categoryRanking?appid={yahoo_app_id}'
    r = requests.get(request_url)
    resp = r.json()

    for i in range(20):
        keyword = resp['category_ranking']['ranking_data'][i]['name']
        # CSVに保存
        save_csv(keyword)

if __name__ == "__main__":
    fetch_yahoo_keyword()