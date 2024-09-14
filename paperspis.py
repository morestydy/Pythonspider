from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
######################### 纬度文献自动登录
## TODO:后续添加数据分析处理功能


def login(word):
    user = 'QTd5RdH'
    password = 'qwe123..'
    url = 'http://spis.hnlat.com/'

    opt = webdriver.ChromeOptions()
    opt.add_experimental_option('detach',True)
    driver = webdriver.Chrome(options=opt)
    driver.get(url)

    input = driver.find_element(By.ID,'field_un')
    chain = ActionChains(driver)
    input.send_keys(user)
    userkey = driver.find_element(By.ID,'field_pw')
    userkey.send_keys(password)
    login = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div/form/div[4]/button')
    chain.click(login).perform()

    wait = WebDriverWait(driver,10)
    wait.until(EC.presence_of_element_located(By.ID,'easy-input'))
    keyword = driver.find_element(By.ID,'easy-input')
    keyword.send_keys(word)
    search_article = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[1]/div/div/div/div[2]/form/button[1]/span[2]')
    year_st = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/input[1]')
    year_st.send_keys('2019')
    btn_eusure = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/button')
    chain.click(btn_eusure).perform()
    # year_end = driver.find_element(By.NAME,'end_y')
    chain.click(search_article).perform()
    with open('paper.text',mode='w',encoding='utf-8') as f:
        f.write(driver.page_source)

if __name__ == '__main__':
    word = input("")
    login(word)