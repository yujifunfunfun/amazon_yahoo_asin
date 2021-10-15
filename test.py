from dotenv import load_dotenv
from logger import set_logger
load_dotenv() #環境変数のロード
from logger import set_logger
logger = set_logger(__name__)
from sp_api.api import Catalog
from sp_api.api import CatalogItems
from sp_api.base.marketplaces import Marketplaces
import re

# item_list = CatalogItems(Marketplaces.JP).search_catalog_items(keywords='イチゴ',pageSize=20)
# print(item_list)

keyword  = 'rr85895858rbmbs86868444'
keyword_truncated = keyword[:15].replace(' ', '　')

p = re.compile(r'(?<!\d)\d{11,12}(?!\d)')
q = re.compile(r'(?<!\d)\d{13,14}(?!\d)')
result = p.search(keyword)


code  = 'rr85895858555566rbmbs86868444'


def fetch_jan_by_code(code):
    p = re.compile(r'(?<!\d)\d{11,12}(?!\d)')
    q = re.compile(r'(?<!\d)\d{13,14}(?!\d)')
    if p.search(code) != None:
            jan = p.search(code).group()
    elif q.search(code) != None:
            jan = q.search(code).group()
    else:
        jan = 'None'
    return jan
