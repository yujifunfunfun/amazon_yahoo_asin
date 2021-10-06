from amazon_sp_api import *
import pandas as pd



def amaozn_category_item():
    category_list =  pd.read_csv("csv/amazon/amazon_category_list.csv").values.tolist()
    for category in category_list:
        item_list = fetch_category_items(category)
            