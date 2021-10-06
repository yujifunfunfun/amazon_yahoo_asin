from amazon_sp_api import *
import pandas as pd



def amazon_store_item():
    store_list =  pd.read_csv("csv/amazon/amazon_store_list.csv").values.tolist()
    for store in store_list:
        item_list = fetch_store_items(store)
            