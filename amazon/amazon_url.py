import re
import csv



def download_target_url():
    csv_file = open('csv/yahoo/yahoo_store_list.csv','r',newline='')
    url_list = [] 
    for row in csv.reader(csv_file):
        store_list.append(row[0])
    return url_list

def fetch_jan_by_code():

    p = re.compile(r'(?<!\d)\d{11,12}(?!\d)')
    q = re.compile(r'(?<!\d)\d{13,14}(?!\d)')
    if p.search(code) != None:
            jan = p.search(code).group()
    elif q.search(code) != None:
            jan = q.search(code).group()
    else:
        jan = 'None'
    return jan