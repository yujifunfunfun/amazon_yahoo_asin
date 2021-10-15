import os
from os.path import join, dirname
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from dotenv import load_dotenv
from logger import set_logger

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

logger = set_logger(__name__)



from sp_api.api import CatalogItems

from sp_api.base.marketplaces import Marketplaces
import pandas as pd

import time


def keyword_modify(keyword_list):
    keyword_truncated_list = []
    for keyword in keyword_list:
        keyword_truncated = keyword[:15].replace(' ', '　')
        keyword_truncated_list.append(keyword_truncated)
    return keyword_truncated_list


def fetch_keyword_search_item_by_amazon(keyword_list):
    page_size = 100
    amazon_item_data = []
    keyword_list = keyword_modify(keyword_list)
    for keyword in keyword_list:
        for page in range(page_size):
            # １ページ目の場合
            if page == 0:
                item_list = CatalogItems(Marketplaces.JP).search_catalog_items(keywords=keyword,pageSize=20)
                item_count = len(item_list.payload.get('items'))
                if item_count == 0:
                    break
                else:
                    next_token = item_list.pagination.get('nextToken')
                    for item in range(item_count):
                        try:
                            asin = item_list.payload.get('items')[item].get('asin')
                            item_name = item_list.payload.get('items')[item].get('summaries')[0].get('itemName')
                            amazon_item_data.append([asin,item_name])
                        except Exception as e:
                            pass
            elif next_token != None:
                item_list = CatalogItems(Marketplaces.JP).search_catalog_items(keywords=keyword,pageSize=20,pageToken=next_token)
                time.sleep(1)
                item_count = len(item_list.payload.get('items'))
                next_token = item_list.pagination.get('nextToken')
                for item in range(item_count):
                    try:
                        asin = item_list.payload.get('items')[item].get('asin')
                        item_name = item_list.payload.get('items')[item].get('summaries')[0].get('itemName')
                        amazon_item_data.append([asin,item_name])
                    except Exception as e:
                        pass
            # 次のページがない場合
            elif next_token == None:
                break
    return amazon_item_data




if __name__ == "__main__":
    fetch_keyword_search_item_by_amazon(['シームレスショーツ ショーツレディース パンツ プレーンショーツ 超盛 ノーマル 女性用 下着 セール','イチゴ'])