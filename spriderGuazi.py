# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient("localhost",27017)
Guazi = client["Guazi"]
xian_carUrl = Guazi["xian_carUrl"]

def sprider_ziru(startpage,endpage):
    host_url ="http://www.guazi.com"
    for page in range(startpage,endpage):
        print('正在处理',page,'页')
        url = host_url+'/xa/buy/o'+str(page)+"/"
        wb_data = requests.get(url)
        Soup = BeautifulSoup(wb_data.text,"lxml")
        carUrllist = Soup.select("div.list-infoBox a")
        for item in carUrllist:
            carUrl = host_url + item.get("href")
            xian_carUrl.insert_one({'url':carUrl})
        time.sleep(2)
    print("final")

if __name__ == '__main__':
    sprider_ziru(1,51)