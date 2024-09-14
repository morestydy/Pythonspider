# 淘宝selenium爬虫商品页面
##### 搜索关键词
##### 分析页码并翻页:得到商品页面码数\模拟翻页\得到后续商品列表
##### 分析提取商品内容:利用PyQuery分析源码,解析得到商品列表
##### 存储至MongoDB:存储至MongoDB


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
# 创建一个未验证的上下文，避免SSL证书的问题
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
url = "https://www.taobao.com/"
opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
opt.add_argument("--log-level=3")  # 设置日志级别为 WARNING
driver = webdriver.Chrome(options=opt)
wait = WebDriverWait(driver, 10)

def save_to_mongo(result):
    try:
        if db[MONGO_TABLE].insert(result):
            print('存储到MONGO成功',result)
    except Exception:
        print('存储到MONGO错误',result)


def search():
    try:
        driver.get(url=url)
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#q")))
        print("查找到input")
        submit = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#J_TSearchForm > div.search-button > button")
            )
        )
        input.send_keys("美食")
        submit.click()
        total = wait.until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "#search-content-leftWrap > div.LeftLay--leftContent--AMmPNfB > div.Pagination--pgWrap--kfPsaVv > div > div > div > button:nth-child(7) > span",
                )
            )
        )
        get_products()
        return total.text
    except TimeoutException:
        search()
def next_page(page_number):
    try:
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#search-content-leftWrap > div.LeftLay--leftContent--AMmPNfB > div.Pagination--pgWrap--kfPsaVv > div > div > span.next-input.next-medium.next-pagination-jump-input')))
        submit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#search-content-leftWrap > div.LeftLay--leftContent--AMmPNfB > div.Pagination--pgWrap--kfPsaVv > div > div > button.next-btn.next-medium.next-btn-normal.next-pagination-jump-go')))
        input.clear()
        input.send_keys(page_number)
        submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#search-content-leftWrap > div.LeftLay--leftContent--AMmPNfB > div.Pagination--pgWrap--kfPsaVv > div > div > div > button.next-btn.next-medium.next-btn-normal.next-pagination-item.next-current'),str(page_number)))
        get_products()
    except TimeoutException:
        next_page(page_number)
def get_products():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#search-content-leftWrap > div.LeftLay--leftContent--AMmPNfB > div.Content--content--sgSCZ12 > div')))
    html = driver.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items
    for item in items:
        product = {
            'image':item.find('.pic .img').attr('src'),
            'price':item.find('.deal').text(),
            'case':item.find('.deal-cnt').text()[:-3],
            'title':item.find('.title').text(),
            'shop':item.find('.shop').text(),
            'location':item.find('.location').text()
    }
    print(product)
    save_to_mongo(product)
def main():
    total = search()
    total = int(re.compile('(\d+)').search(total).group(1))
    # print(total)
    for i in range(2,total+1):
        next_page(i)
    driver.close()

if __name__ == "__main__":
    main()
