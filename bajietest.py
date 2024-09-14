import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from pyquery import PyQuery as pq
import time
import ssl
from config import *
import pymongo
url = 'https://www.zbj.com/fw/?k=LOGO设计'
# response = requests.get(url=url,headers={
#     'User-Agent':UserAgent().random
# })
# response.encoding = response.apparent_encoding
# response.raise_for_status()
# with open('./bajie.txt','w',encoding='utf-8') as f:
#     f.write(response.text)
#     print('写入成功')

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# opt = webdriver.ChromeOptions()
# opt.add_experimental_option("detach", True)
# opt.add_argument("--log-level=3")  # 设置日志级别为 WARNING
# driver = webdriver.Chrome(options=opt)
# wait = WebDriverWait(driver, 10)
# driver.get(url=url)
# while True:
#     # 滑动到最底部，加载出所有图片
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)
#     # 检测是不是到最底部了
#     if driver.execute_script("return window.innerHeight + window.pageYOffset >= document.body.offsetHeight;"):
#         break
# with open('bajie.txt', 'w', encoding='utf-8') as file:
#     file.write(driver.page_source)
# time.sleep(8)
# driver.close()
MONGO_URL = 'localhost'
MONGO_DB = 'bajie'
MONGO_TABLE = 'producttest'

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
with open('bajie.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    # 解析内容
    doc = pq(content)
    items = doc('.search-result-list-service .service-card-wrap').items()
    # print(type(items))
    for item in items:
        price = item.find('.bot-content .price').text()
        image = item.find('.el-carousel__item.is-active.is-animating img').attr('src')
        title = item.find('.name-pic-box a span').text().replace('\n','')
        sales = item.find('.el-tooltip.sale.item .num').text()
        score = item.find('.el-tooltip.comment.item .num').text()
        shop_score = item.find('.shop-detail .shop-score').text()
        shop_name = item.find('.shop-detail .shop-info.text-overflow-line').text()
        # print(price)
        # print(image)
        # print(title)
        # print(sales)#sales
        # print(score)#score
        # print(shop_score)#shop-score
        # print(shop_name)#name
        product = {
            'title':title,
            'img':image,
            'price':price,
            'sales':sales,
            'score':score,
            'shopscore':shop_score,
            'shopname':shop_name
        }
        print(product)
        try:
            if db[MONGO_TABLE].insert_one(product):
                print('存储到MongoDB成功',product)
        except Exception:
            print('存储到MongoDB失败',product)

