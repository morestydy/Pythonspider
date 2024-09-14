from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import requests
import time
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import pandas as pd
import re

pictures = pd.DataFrame(columns=['title','link'])

for page in range(2,11):
    url = f'https://pic.netbian.com/index_{page}.html'
    opt = webdriver.ChromeOptions()
    # opt.add_experimental_option('detach',True)
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    # print(driver.page_source)
    # with open('netbian.txt','w',encoding='utf-8') as f:
    #     f.write(driver.page_source)
    # with open('netbian.txt','r',encoding='utf-8') as f:
    #     source = f.read()
    # soup = BeautifulSoup(driver.page_source,'html.parser')
    soup = BeautifulSoup(driver.page_source,'html.parser')
    # print(soup)
    headers = {
        'User-Agent':UserAgent().random
    }
    pic_list = soup.find('div',attrs={'class':'slist'})
    pics_list = pic_list.find('ul',attrs={'class':'clearfix'})
    # print(pics_list)
    netbians = pics_list.find_all('li')

    for netbian in netbians:
        try:
        # print(netbian)
            link = netbian.a.img['src']
            pic_link = 'https://pic.netbian.com/'+link
            # print(pic_link)
            title = netbian.a.b.string
            # print(title)
            pic_info = {
                'link':pic_link,
                'title':title.strip(),
            }
            pictures = pictures._append(pic_info,ignore_index = True)
            print('写入:'+title+'src='+pic_link)
            safe_title = re.sub(r'[<>:"/\\|?*]', '', title)  # 清理不合法字符
            img_content = requests.get(pic_link,headers=headers).content
            with open(f'netbian\\{safe_title}.jpg','wb') as f:
                f.write(img_content)
                print(f'图片{title}写入')
        except TypeError:
            break
pictures.to_excel('netbian.xlsx',index=False)