from amazon_sp_api import *
import pandas as pd


def keyword_modify(csv_path):
    keyword_list = pd.read_csv(csv_path).values.tolist()
    keyword_truncated_list = []
    for keyword in keyword_list:
        keyword = keyword[0]
        keyword_truncated = keyword[:15].replace(' ', '　')
        keyword_truncated_list.append(keyword_truncated)
    return keyword_truncated_list




def fetch_yahoo_highrate_store_item_by_amazon():
    keyword_list = keyword_modify("csv/yahoo/yahoo_highrate_storeitem.csv")
    page_size = 5
    amazon_item_list_yahoo_highrate_store = []
    for keyword in keyword_list:
        for page in range(page_size):
            if page == 0:
                item_list = CatalogItems(Marketplaces.JP).search_catalog_items(keywords=keyword,pageSize=20)
                item_count = len(item_list.payload.get('items'))
                if item_count == 0:
                    break
                else:
                    next_token = item_list.pagination.get('nextToken')
                    for item in range(item_count):
                        asin = item_list.payload.get('items')[item].get('asin')
                        item_name = item_list.payload.get('items')[item].get('summaries')[0].get('itemName')
                        amazon_item_list_yahoo_highrate_store.append([asin,item_name])
            elif next_token != None:
                item_list = CatalogItems(Marketplaces.JP).search_catalog_items(keywords=category,pageSize=20,pageToken=next_token)
                item_count = len(item_list.payload.get('items'))
                next_token = item_list.pagination.get('nextToken')

                for item in range(item_count):
                    asin = item_list.payload.get('items')[item].get('asin')
                    item_name = item_list.payload.get('items')[item].get('summaries')[0].get('itemName')
                    amazon_item_list_yahoo_highrate_store.append([asin,item_name])
            elif next_token == None:
                break
    print(len(amazon_item_list_yahoo_highrate_store))



            
def fetch_yahoo_keyword_ranking_item_by_amazon():
    keyword_list =  pd.read_csv("csv/yahoo/yahoo_keyword_list.csv").values.tolist()
    for keyword in keyword_list:
        item_list = fetch_keyword_items(keyword)

def fetch_yahoo_category_ranking_item_by_amazon():
    keyword_list =  pd.read_csv("csv/yahoo/yahoo_category_ranking.csv").values.tolist()
    for keyword in keyword_list:
        item_list = fetch_keyword_items(keyword)


if __name__ == "__main__":
    amazon_fetch_category_item()