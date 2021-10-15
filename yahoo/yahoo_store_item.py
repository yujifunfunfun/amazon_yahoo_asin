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
import re
import time

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

logger = set_logger(__name__)


yahoo_app_id = os.environ.get("YAHOO_APP_ID")

def download_target_store():
    csv_file = open('csv/yahoo/yahoo_store_list.csv','r',newline='')
    store_list = [] 
    for row in csv.reader(csv_file):
        store_list.append(row[0])
    return store_list

def fetch_jan_by_code(code):
    p = re.compile(r'(?<!\d)\d{11,12}(?!\d)')
    q = re.compile(r'(?<!\d)\d{13,14}(?!\d)')
    if p.search(code) != None:
            jan = p.search(code).group()
    elif q.search(code) != None:
            jan = q.search(code).group()
    else:
        jan = 'None'
    return jan


def fetch_yahoo_item_data():
    item_list = []
    store_list = download_target_store()
    for store in store_list:
        store = urllib.parse.quote(store)
        request_url = f'https://shopping.yahooapis.jp/ShoppingWebService/V3/itemSearch?appid={yahoo_app_id}&seller_id={store}&results=50&start=1&sort=-score'
        r = requests.get(request_url)
        resp = r.json()
        total_req_count = 21
        page_item = resp['totalResultsReturned']
        for count in range(total_req_count):
            start = count*50+1
            try:            
                if count != 0:
                    request_url = f'https://shopping.yahooapis.jp/ShoppingWebService/V3/itemSearch?appid={yahoo_app_id}&seller_id={store}&results=50&start={start}&sort=-score'
                    r = requests.get(request_url)
                    time.sleep(1)
                    resp = r.json()
                for i in range(page_item):
                    try:
                        review_rate = resp['hits'][i]['review']['rate']
                        if review_rate < 4.9:
                            pass
                        else:
                            item_name = resp['hits'][i]['name']
                            code = resp['hits'][i]['code']
                            jan = fetch_jan_by_code(code)
                            data =[jan,item_name]            
                            item_list.append(data)
                    except Exception as e:
                        pass
            except Exception as e:
                pass
    return item_list

if __name__ == "__main__":
    fetch_yahoo_item_data()