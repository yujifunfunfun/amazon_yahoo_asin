from dotenv import load_dotenv
from logger import set_logger
load_dotenv() #環境変数のロード
from logger import set_logger
logger = set_logger(__name__)
from sp_api.api import Catalog
from sp_api.api import CatalogItems

from sp_api.base.marketplaces import Marketplaces
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import os
from time import sleep
import re
import pandas as pd


def start_chrome():
    user_agent = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    ]
    UA = user_agent[random.randrange(0, len(user_agent), 1)]
    global option
    option = Options()  
    option.add_argument('--lang=ja-JP')
    option.add_argument('--headless')
    option.add_argument('--user-agent=' + UA)
    option.add_argument('--ignore-certificate-errors')
    option.add_argument('--ignore-ssl-errors')
    option.add_argument("window-size=1000,800")
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=option) 
    



def asin_to_jan(amazon_item_list):
    start_chrome()
    wait = WebDriverWait(driver, 10)
    amazon_item_data_list = []
    n = 100
    amazon_item_list_per_100 = [amazon_item_list[i:i + n] for i in range(0, len(amazon_item_list), n)]
    for amazon_item_100 in amazon_item_list_per_100:
        asin_list = []
        for amazon_item in amazon_item_100:
            asin = amazon_item[0]
            asin_list.append(asin)
        asin_100 = ','.join(map(str,asin_list))
        driver.get("https://caju.jp/bulk/convert")
        element = wait.until(EC.visibility_of_all_elements_located)
        driver.execute_script(f'document.getElementById("bulkKeywords").value="{asin_100}"')
        driver.find_element_by_id('bulkSubmit').click()
        element2 = wait.until(EC.visibility_of_all_elements_located)

        for i,n in zip(range(3,202,2),range(2,201,2)):
            try:
                asin = driver.find_element_by_xpath(f'/html/body/div/div/div[5]/div[1]/div[{i}]/div/div[2]/span[1]').text
                jan = driver.find_element_by_xpath(f'/html/body/div/div/div[5]/div[1]/div[{i}]/div/div[2]/span[2]').text
                item_name = driver.find_element_by_xpath(f'/html/body/div/div/div[5]/div[1]/div[{n}]/div/span/b').text
                amazon_item_data_list.append([asin,jan,item_name])
            except Exception as e:
                pass
    amazon_item_df = pd.DataFrame(amazon_item_data_list,columns=['ASIN','JAN','商品名'])
    
    return amazon_item_df


if __name__ == "__main__":
    start_chrome()
    asin_to_jan([['B08L7MS18T','aaa'],['B07G4QQYP7','bbb'],['B09BJP7Q1R','ccc'],['B09CM5GQRP','ddd']])


