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
import math

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

logger = set_logger(__name__)

yahoo_app_id = os.environ.get("YAHOO_APP_ID")



def fetch_yahoo_category_ranking_item():
    request_url = f'https://shopping.yahooapis.jp/ShoppingWebService/V2/categoryRanking?appid={yahoo_app_id}'
    r = requests.get(request_url)
    resp = r.json()
    keyword_list = []
    for i in range(20):
        keyword = resp['category_ranking']['ranking_data'][i]['name']
        keyword_list.append(keyword)
    return keyword_list

if __name__ == "__main__":
    fetch_yahoo_category_ranking_item()