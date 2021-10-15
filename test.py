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

keyword  = 'https://www.amazon.co.jp/2019%E6%9C%80%E6%96%B0%E7%89%88-IPL%E5%85%89%E8%84%B1%E6%AF%9B%E5%99%A8-%E5%AE%B6%E5%BA%AD%E7%94%A8%E8%84%B1%E6%AF%9B%E5%99%A8-%E3%83%93%E3%82%AD%E3%83%8B%E3%83%A9%E3%82%A4%E3%83%B3-%E6%97%A5%E6%9C%AC%E8%AA%9E%E8%AA%AC%E6%98%8E%E6%9B%B8%E4%BB%98%E3%81%8D/dp/B07YFCS19H/?_encoding=UTF8&pd_rd_w=hryrY&pf_rd_p=accd8b8e-bcce-45fb-8bd2-53a49bf56dfc&pf_rd_r=6GH7PP30VVT6QCPR3S7D&pd_rd_r=14cefbd6-d1f9-4a56-9b21-4f602ccb181f&pd_rd_wg=xUD0M&ref_=pd_gw_ci_mcx_mr_hp_atf_m'
keyword_truncated = keyword[:15].replace(' ', '　')

p = re.compile(r'[^0-9A-Z]([0-9A-Z]{10})([^0-9A-Z]|$)')
q = r'/(.*)/'  
result = p.search(keyword).group(1)
# asin = re.search(p, keyword).group(1)
print(result)

  