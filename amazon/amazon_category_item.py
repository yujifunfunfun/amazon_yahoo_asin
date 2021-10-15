import os
import sys
from dotenv import load_dotenv
load_dotenv() #環境変数のロード
from sp_api.api import CatalogItems
from sp_api.base.marketplaces import Marketplaces
import pandas as pd
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))


def amazon_fetch_category_item():
    category_list =  pd.read_csv("csv/amazon/amazon_category_item_list.csv").values.tolist()
    page_size = 5
    amazon_category_item_list = []
    for category in category_list:
        category = category[0]
        for page in range(page_size):
            if page == 0:
                item_list = CatalogItems(Marketplaces.JP).search_catalog_items(keywords=category,pageSize=20)
                item_count = len(item_list.payload.get('items'))
                if item_count == 0:
                    break
                else:
                    next_token = item_list.pagination.get('nextToken')
                    for item in range(item_count):
                        asin = item_list.payload.get('items')[item].get('asin')
                        item_name = item_list.payload.get('items')[item].get('summaries')[0].get('itemName')
                        amazon_category_item_list.append([asin,item_name])
            elif next_token != None:
                item_list = CatalogItems(Marketplaces.JP).search_catalog_items(keywords=category,pageSize=20,pageToken=next_token)
                time.sleep(1)
                item_count = len(item_list.payload.get('items'))
                next_token = item_list.pagination.get('nextToken')

                for item in range(item_count):
                    asin = item_list.payload.get('items')[item].get('asin')
                    item_name = item_list.payload.get('items')[item].get('summaries')[0].get('itemName')
                    amazon_category_item_list.append([asin,item_name])
            elif next_token == None:
                break
    print(len(amazon_category_item_list))


if __name__ == "__main__":
    amazon_fetch_category_item()





            