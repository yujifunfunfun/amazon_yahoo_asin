from amazon_sp_api import *
import pandas as pd



def fetch_yahoo_highrate_store_item_by_amazon():
    keyword_list =  pd.read_csv("csv/yahoo/yahoo_highrate_storeitem.csv").values.tolist()
    for keyword in keyword_list:
        item_list = fetch_keyword_items(keyword)
            
def fetch_yahoo_keyword_ranking_item_by_amazon():
    keyword_list =  pd.read_csv("csv/yahoo/yahoo_keyword_list.csv").values.tolist()
    for keyword in keyword_list:
        item_list = fetch_keyword_items(keyword)

def fetch_yahoo_category_ranking_item_by_amazon():
    keyword_list =  pd.read_csv("csv/yahoo/yahoo_category_ranking.csv").values.tolist()
    for keyword in keyword_list:
        item_list = fetch_keyword_items(keyword)
