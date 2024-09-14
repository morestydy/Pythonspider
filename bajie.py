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


client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
url = "https://www.zbj.com/?fr=frzpheader"
k = 'LOGO设计'
opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
opt.add_argument("--log-level=3")  # 设置日志级别为 WARNING
driver = webdriver.Chrome(options=opt)
wait = WebDriverWait(driver, 10)

def search():
    try:
        driver.get(url=url)
        while True:
            # 滑动到最底部，加载出所有图片
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            # 检测是不是到最底部了
            if driver.execute_script("return window.innerHeight + window.pageYOffset >= document.body.offsetHeight;"):
                break
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#j-header-searchform > div > input')))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#j-header-searchform > button')))
        input.send_keys(k)
        submit.click()
        print(driver.window_handles)
        driver.switch_to.window(driver.window_handles[1])
        # total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#__layout > div > div:nth-child(3) > div > div.search-content-wrap > div > div.search-result-list.search-result-list-add > div.search-result-list-left > div.page-wrap.clearfix > ul > li:nth-child(8) > a')))
        total = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[2]/div[1]/div[3]/ul/li[8]/a')))
        get_products()
        return total.text
    except TimeoutException:
        search()
def next_page():
    try:
        while True:
            # 滑动到最底部，加载出所有图片
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            # 检测是不是到最底部了
            if driver.execute_script("return window.innerHeight + window.pageYOffset >= document.body.offsetHeight;"):
                break
        btn_next = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.li-page i.el-icon-arrow-right')))
        # chains = ActionChains(driver)
        # chains.click(btn_next).perform()
        driver.execute_script("arguments[0].click();", btn_next)
        get_products()
    except TimeoutException:
        next_page()
def get_products():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.search-result-list-service .service-card-wrap .serve-item')))
    print('获得item')
    
    html = driver.page_source
    doc = pq(html)
    items = doc(".search-result-list-service .service-card-wrap").items()
    for item in items:
        link = item.find('.el-carousel__item.is-active.is-animating img').attr.src
        price = item.find('.bot-content .price').text()
        title = item.find('.name-pic-box a span').text().replace('\n','')
        sales = item.find('.el-tooltip.sale.item .num').text()#sales
        score = item.find('.el-tooltip.comment.item .num').text()#score
        shopscore = item.find('.shop-detail .shop-score').text()#shop-score
        shopname = item.find('.shop-detail .shop-info.text-overflow-line').text()#name
        print(link)
        print(price)
        print(title)
        product = {
            'title':title,
            'img':link,
            'price':price,
            'sales':sales,
            'score':score,
            'shopscore':shopscore,
            'shopname':shopname
        }
        save_to_mongo(product)
        with open('result.txt','a',encoding = 'utf-8') as f:
            f.write(f"Title: {title}\n")
            f.write(f"Image URL: {link}\n")
            f.write(f"Price: {price}\n")
            f.write(f"Sales: {sales}\n")
            f.write(f"Score: {score}\n")
            f.write(f"Shop Score: {shopscore}\n")
            f.write(f"Shop Name: {shopname}\n")
            f.write('\n')
        # time.sleep(2)
def save_to_mongo(result):
    try:
        if db[MONGO_TABLE].insert_one(result):
            print('存储到MongoDB成功',result)
    except Exception:
        print('存储到MongoDB失败',result)

def main():
    total = int(search())
    print(total)
    for i in range(2,(total-80)):
        next_page()
        print(f'识别到bnt_next{i}')
    driver.close()

if __name__ == '__main__':
    main()

