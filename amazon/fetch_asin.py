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

from sp_api.api import Catalog
from sp_api.base.marketplaces import Marketplaces
import pandas as pd
import eel
import time


def fetch_asin(yahoo_item_data):
    cols = ['JAN','ASIN','商品名']
    yahoo_item_df = pd.DataFrame(columns=cols)
    for yahoo_item in yahoo_item_data:
        try:
            jan = yahoo_item[0]
            asin = Catalog(Marketplaces.JP).list_items(JAN=jan).payload.get('Items')[0].get('Identifiers').get('MarketplaceASIN').get('ASIN')
            time.sleep(1)
            yahoo_item.insert(1,asin)
            record = pd.Series(yahoo_item, index=yahoo_item_df.columns)
            yahoo_item_df = yahoo_item_df.append(record, ignore_index=True)
        except Exception as e:
            yahoo_item.insert(1,'None')
            record = pd.Series(yahoo_item, index=yahoo_item_df.columns)
            yahoo_item_df = yahoo_item_df.append(record, ignore_index=True)
    return yahoo_item_df



if __name__ == "__main__":
    fetch_asin([['9784905319443','djdj'],['4589440870269','yyhy'],['8414852021830','sjsj']])


