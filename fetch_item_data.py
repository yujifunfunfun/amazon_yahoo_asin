from yahoo.yahoo_store_item import *
from yahoo.yahoo_keyword_ranking_bs import *
from yahoo.yahoo_category_ranking import *
from amazon.amazon_keyword_item import *
from amazon.fetch_asin import *
from asin_to_jan import *
import pandas as pd
import numpy as np
import eel

def fetch_item_data(filter_list):
    eel.view_log_js('商品情報取得中...')
    if 'yahoo_store' in filter_list:
        # ヤフショの高評価ストア商品取得
        yahoo_item_data = fetch_yahoo_item_data()
        yahoo_item_df = fetch_asin(yahoo_item_data)
        yahoo_item_df.index = np.arange(1,len(yahoo_item_df)+1)
        yahoo_item_df.to_csv("yahoo_store_item.csv,encoding='shift-jis'")
        yahoo_item_name_list = []
        for yahoo_item in yahoo_item_data:
            yahoo_item_name = yahoo_item[1]
            yahoo_item_name_list.append(yahoo_item_name)  
                  
        amazon_item_list = fetch_keyword_search_item_by_amazon(yahoo_item_name_list)
        amazon_item_df = asin_to_jan(amazon_item_list)
        amazon_item_df.index = np.arange(1,len(amazon_item_df)+1)
        amazon_item_df.to_csv("yahoo_store_item_amazon.csv,encoding='shift-jis'")
        logger.info('高評価ストア商品検索完了')
        eel.view_log_js('高評価ストア商品検索完了')

    if 'yahoo_ranking' in  filter_list:
        # keyword_ranking_list = fetch_yahoo_keyword_bs()
        keyword_ranking_list = ['まつ毛美容液', '浴槽']
        amazon_item_list = fetch_keyword_search_item_by_amazon(keyword_ranking_list)
        amazon_item_df = asin_to_jan(amazon_item_list)
        amazon_item_df.index = np.arange(1,len(amazon_item_df)+1)
        amazon_item_df.to_csv("yahoo_keyword_ranking_item_amazon.csv,encoding='shift-jis'")
        logger.info('売れ筋ランキング商品検索完了')
        eel.view_log_js('売れ筋ランキング商品検索完了')


    if 'yahoo_category_ranking' in filter_list:
        category_ranking_list = fetch_yahoo_category_ranking_item()
        amazon_item_list = fetch_keyword_search_item_by_amazon(category_ranking_list)
        amazon_item_df = asin_to_jan(amazon_item_list)
        amazon_item_df.index = np.arange(1,len(amazon_item_df)+1)
        amazon_item_df.to_csv("yahoo_category_ranking_item_amazon.csv,encoding='shift-jis'")
        logger.info('カテゴリーランキング商品検索完了')
        eel.view_log_js('カテゴリーランキング商品検索完了')

    eel.view_log_js('処理を終了します')
    

    # if 'category' in filter_list:
    #     category_list =  pd.read_csv("amazon_category_list.csv").values.tolist()
    #     amazon_item_list = fetch_keword_search_item_by_amazon(category_list)
    #     amazon_item_df = asin_to_jan(amazon_item_list)
    #     amazon_item_df.to_csv("yahoo_keyword_ranking_item.csv")




if __name__ == "__main__":
    fetch_item_data('yahoo_category_ranking')

