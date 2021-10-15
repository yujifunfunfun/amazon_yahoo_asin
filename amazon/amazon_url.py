import re
import csv
import numpy as np

def download_target_url():
    csv_file = open('csv/amazon/amazon_url_list.csv','r',newline='')
    url_list = [] 
    for row in csv.reader(csv_file):
        url_list.append(row[0])
    return url_list

def fetch_asin_by_url():
    url_list = download_target_url()
    asin_list = []
    p = re.compile(r'[^0-9A-Z]([0-9A-Z]{10})([^0-9A-Z]|$)')
    for url in url_list:
        try:
            asin = p.search(url).group(1)
            asin_list.append([asin,url])
        except Exception as e:
            pass
    np.savetxt("asin_list.csv", asin_list, delimiter =",",fmt ='% s')

if __name__ == "__main__":
    fetch_asin_by_url()
