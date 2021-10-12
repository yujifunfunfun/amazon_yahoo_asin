from amazon_sp_api import *
import pandas as pd



def amazon_fetch_store_item():
    store_list =  pd.read_csv("csv/amazon/amazon_store_list.csv").values.tolist()
    for store in store_list:
        res = Catalog(Marketplaces.JP).list_items(Query='A1ZLLAC8MKRGW')
        


if __name__ == "__main__":
    amazon_fetch_store_item()