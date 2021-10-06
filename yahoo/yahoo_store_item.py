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

def download_target_store():
    csv_file = open('csv/yahoo_store_list.csv','r',newline='')
    store_list = [] 
    for row in csv.reader(csv_file):
        store_list.append(row[0])
    return store_list

def save_csv(data):
    with open('csv/yahoo_highrate_storeitem.csv','a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def fetch_yahoo_item_data():
    store_list = download_target_store()
    for store in store_list:
        store = urllib.parse.quote(store)
        request_url = f'https://shopping.yahooapis.jp/ShoppingWebService/V3/itemSearch?appid={yahoo_app_id}&query={store}'
        r = requests.get(request_url)
        resp = r.json()
        total_item = resp['totalResultsAvailable']
        total_req_count = math.floor(total_item / 50)

        for count in range(total_req_count+1):
            start = count*50+1
            request_url = f'https://shopping.yahooapis.jp/ShoppingWebService/V3/itemSearch?appid={yahoo_app_id}&query={store}&results=50&start={start}&sort=-score'
            r = requests.get(request_url)
            resp = r.json()
            try:
                for i in range(50):
                    review_rate = resp['hits'][i]['review']['rate']
                    if review_rate < 3:
                        pass
                    else:
                        item_name = resp['hits'][i]['name']
                        jan = resp['hits'][i]['janCode']
                        data =[jan,item_name]
                        # CSVに保存
                        save_csv(data)
            except Exception as e:
                pass

if __name__ == "__main__":
    fetch_yahoo_item_data()