import os
from dotenv import load_dotenv
from logger import set_logger
load_dotenv() #環境変数のロード
from logger import set_logger
logger = set_logger(__name__)
from sp_api.api import Catalog
from sp_api.api import CatalogItems

from sp_api.base.marketplaces import Marketplaces



def fetch_store_items(store):
    res = CatalogItems(Marketplaces.JP).search_catalog_items(keywords='ペット用品',pageSize=20)
    return res

def fetch_category_items(category):
    res = Catalog(Marketplaces.JP).list_items(category)
    return res

def fetch_keyword_items(keyword):
    res = Catalog(Marketplaces.JP).list_items(keyword)
    return res