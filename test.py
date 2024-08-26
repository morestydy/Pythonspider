# 1. 爬虫https://ssr1.scrape.center/page/,图片 标题 分数


# import requests
# from fake_useragent import UserAgent
# import pandas as pd
# import re
# movies_data=pd.DataFrame(columns=['title','score','link'])
# with open('E:\\python\\pythonspider\\movie.txt','r',encoding='utf-8') as f:
#     html = f.read()
#     # print(html)
#     title_list = re.findall(r'<a data-v-7f856186.*?src="(.*?.jpg)@.*?cover">.*?class="m-b-sm">(.*?)</h2>.*?<p.*?score.*?>(.*?)</p>',html,re.S)
#     movie_recore = {}
#     for pic,title,score in title_list:
#         safe_title = re.sub(r'[<>:"/\\|?*\x00-\x1F]', '', title)
#         print(f'pic:{pic},title:{safe_title},score:{score}')
#         movie_recore['title'] = ''.join(safe_title.strip())
#         movie_recore['score'] = ''.join(score.strip())
#         movie_recore['link'] = ''.join(pic.strip())

#     movies_data = movies_data._append(movie_recore,ignore_index=True)
# movies_data.to_excel('movies.xlsx', index=False)

################################################################################
# import requests
# from fake_useragent import UserAgent
# import pandas as pd
# import re



# movies=pd.DataFrame(columns=['title','score','link'])
# movies_data=pd.DataFrame(columns=['title','score','link'])
# # movie_record = {}
# for pages in range(1,10):
#     headers = {
#         'UserAgent':UserAgent().random
#     }
#     url=r'https://ssr1.scrape.center/page/'+str(pages)
#     response = requests.get(url,headers=headers)
#     response.raise_for_status()
#     response.encoding = response.apparent_encoding
#     # print(response.status_code)
#     title_list = re.findall(r'<a data-v-7f856186.*?src="(.*?.jpg)@.*?cover">.*?class="m-b-sm">(.*?)</h2>.*?<p.*?score.*?>(.*?)</p>',response.text,re.S)
#     # print(title_list)
#     for link,title,score in title_list:
#         safe_title = re.sub(r'[<>:"/\\|?*\x00-\x1F]', '', title)
#         print(f'pic:{link},title:{safe_title},score:{score}')
#         # 图片下载
#         img_content = requests.get(link,headers=headers).content
#         with open(f'pic\\{safe_title}.jpg',mode='wb') as f:
#             f.write(img_content)
#         movie_record = {
#             'title': safe_title,
#             'score': score.strip(),
#             'link': link.strip()
#         }
#         movies_data = movies_data._append(movie_record,ignore_index=True)
# movies_data.to_excel('movies.xlsx', index=False)


# 导入请求和解析数据模块


# import pandas as pd
# import requests
# from fake_useragent import UserAgent
# import time
# import re

# # url = 'https://www.maoyan.com/board/4?offset=10'
# # headers = {'User-Agent':UserAgent().random}
# # response = requests.get(url=url,headers=headers)
# # response.raise_for_status()
# # response.encoding = response.apparent_encoding
# # print(response.status_code)
# # print(response.url)
# # with open('maoyan.txt','w',encoding='utf-8') as f:
# #     f.write(response.text)
# ########################################猫眼#################
# # movies_date = pd.DataFrame(columns=['title','stars','releasetime','score','link'])
# # headers = {'User-Agent':UserAgent().random}
# # with open('maoyan.txt','r',encoding='utf-8') as f:
# #     html = f.read()
# #     movie_list = re.findall('<dd>.*?<img data-src="(.*?)".*?<p class="name">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">上映时间：(.*?)</p>.*?<p class="score"><i class="integer">(.*?)</i><i class="fraction">(.*?)</i></p>.*?</dd>',html,re.S)
# #     # print(movie_list)
# #     for link,title,stars,releasetime,integer,fraction in movie_list:
# #         # print(f'link:{link},title:{title},stars:{stars},releasetime:{releasetime},score:{integer}{fraction}')
# #         mov_record={
# #             'title':title.replace('主演：',''),
# #             'stars':stars.strip(),
# #             'releasetime':releasetime,
# #             'score':integer+fraction,
# #             'link':link.strip()
# #         }
#         # img_content = requests.get(link,headers=headers).content
#         # with open(f'maoyan\\{title}.jpg','wb') as f:
#         #     f.write(img_content)
#         # print(mov_record['title'])
# #         movies_date=movies_date._append(mov_record,ignore_index=True)
# # movies_date.to_excel('douban.xlsx',index=False)

#################################XPath
# from lxml import etree

# # Xpath解析HTML页面只需要三个步骤。！！！可以解析html，也可以解析xml。
# #               1. 构造xpath对象（把html字符串转换成xpath对象）
# #               2. 编写选择器（最重要） 这个主要可以通过节点的属性，节点相互之间的层级关系，进行选择，一般最后都是//text()|@属性名
# #               3. 取出需要的text数据
# text = '''
# <!DOCTYPE html>
# <html lang="en">
#   <head>
#     <meta charset="UTF-8" />
#     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
#     <title>Document</title>
#   </head>
#   <body>
#     <div>
#       <ul>
#         <li class="item-0"><a href="link1.html">first item</a></li>
#         <li class="item-1 li" name="li-2">
#           <a href="link2.html">second item</a>
#         </li>
#         <li class="item-inactive"><a href="link3.html">third item</a></li>
#         <li class="item-1"><a href="link4.html">fourth item</a></li>
#         <li class="item-0"><a href="link5.html">fifth item</a></li>
#       </ul>
#     </div>
#   </body>
# </html>
# '''


# # 使用HTML可以自动修正html结果，html为bytes类型
# html = etree.HTML(text)
# result = etree.tostring(html)
# # print(result.decode('utf-8'))
# # 从外部导入HTML文件并解析
# new_html = etree.parse('test.html', etree.HTMLParser())
# # 获取文件调用etree里面的xpath方法就可以解析出节点了，学习xpath的过程就是写选择器的过程
# # 1.选取所有节点
# result0 = new_html.xpath('//*')

# # 2.选取子节点，使用/获取子节点，使用//获取子孙节点。注意层级的关系
# result1 = html.xpath('//ul/li')  # 选取ul里面的所有li，只会直接选中，不会跨层级选中
# result2 = html.xpath('//ul//a')  # 选取ul里面的所有a，会跨层级选中
# # print(result1)

# # 3.根据子节点的属性选择到父节点，类似于相对路径
# result3 = html.xpath('//a[@href="link4.html"]/../@class')  # 根据属性选择器选择到a标签。利用../回到父级获取父级的class属性

# # 4.根据节点里面的class类进行选择
# result4 = new_html.xpath('//li[@class="item-0"]')

# # 5.获取节点中的文本，使用text()函数。
# # 如果直接匹配子节点，可能会匹配到其他子节点的数据。/n之类的。这里是因为自动添加了</li>标签，自动换行。
# result5 = html.xpath('//li[@class="item-0"]//text()')
# result6 = html.xpath('//li[@class="item-0"]/a/text()')

# # 6.获取节点的属性，使用@href
# result7 = html.xpath('//li/a/@href')  # 获取所有li下面的所有a的href属性

# # 7.根据多个属性值进行匹配，采用contains方法.只有包含这个属性就被筛选出来
# result8 = html.xpath('//li[contains(@class,"li")]/a/text()')  # 查找li里面class属性下面包含li的a标签的值

# # 8.根据多个属性的值进行匹配，利用and运算符
# result9 = html.xpath('//li[contains(@class,"li") and @name="li-2"]/a/text()')  # 筛选出类名包含li的，name值为li-2的li，
# # 并且求出它下面的text值

# # 9.按序选择，匹配到多个节点后，选择多个节点当中的第几个
# result10 = html.xpath('//li[1]/a/text()')  # 选择第一个li里面的a的text值
# result11 = html.xpath('//li[last()]/a/text()')  # 选择最后一个li里面的a的值
# result12 = html.xpath('//li[position()>3]/a/text()')  # 选择3以后的li标签下面的a的值

# # 10.选取跟本节点相关的节点

# result13 = html.xpath('//li[1]/ancestor::*')  # 获取第一个li的所有父节点，递归获取，会往上继续找
# result14 = html.xpath('//li[1]/ancestor::div')  # 获取所有父节点，但是只要div标签的
# result15 = html.xpath('//li[1]/attribute::*')  # 获取当前li节点的所有属性值
# result16 = html.xpath('//li[1]/child::a[@href="link1.html"]')  # 获取当前li节点的子节点，并且需要满足href=link1.html条件
# result17 = html.xpath('//li[1]/descendant::span')  # 获取当前li节点的所有子孙节点，但是只要span标签的
# result18 = html.xpath('//li[1]/following::*[2]')  # 获取当前节点之后的所有节点（不是同级的），但是只要第2个。就是a
# result19 = html.xpath('//li[1]/following-sibling::*')  # 获取当前节点之后的所有节点（是同级的）。

# # for循环专门打印运行结果
# for i in range(0, 20):
#     print(f'result{i}: {locals()["result" + str(i)]}')
#     print('--------------------------')

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# import ssl
# import time
# # 创建一个未验证的上下文，避免SSL证书的问题
# context = ssl.create_default_context()
# context.check_hostname = False
# context.verify_mode = ssl.CERT_NONE

# 加载谷歌浏览器驱动
# driver_path = r'E:\\download\\chromedriver-win64'
# ser = Service(driver_path)

##申明浏览器对象
# driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Edge()

# option = webdriver.ChromeOptions()
# option.add_experimental_option("detach", True) #运行结束时不关闭浏览器
# driver = webdriver.Chrome(options=option)
# option = webdriver.ChromeOptions()
# option.add_experimental_option("detach", True)
# option.add_argument('--ignore-certificate-errors')
# driver = webdriver.Chrome(options=option)
# driver.maximize_window()  # 设置页面最大化，避免元素被隐藏

# driver.get('https://www.taobao.com')
###############单个元素
# input_first = driver.find_element(By.ID,'q')
# input_second = driver.find_element(By.CSS_SELECTOR,'#q')
# input_third = driver.find_element(By.XPATH,'//*[@id="q"]')

# '''
# find_element(By.ID)
# find_element(By.XPATH)
# find_element(By.LINK_TEXT)
# find_element(By.NAME)
# find_element(By.CSS_SELECTOR)
# find_element(By.CLASS_NAME)
# find_element(By.TAG_NAME)
# print(input_first, input_second, input_third)
# driver.close()
# '''
############ 多个元素
# driver.implicitly_wait(10)
# lis = driver.find_elements(By.CSS_SELECTOR,'.service-bd--vV7Az7uc li')
# print(lis)
########### 元素相互操作
# input = driver.find_element(By.ID,'q')
# input.send_keys('IPhone')
# time.sleep(5)
# input.clear()
# input.send_keys('iPad')
# button = driver.find_element(By.CLASS_NAME,'btn-search')
# button.click()
########################交互操作 ActionChains

# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By

# option = webdriver.ChromeOptions()
# option.add_experimental_option("detach", True)
# option.add_argument('--ignore-certificate-errors')
# driver = webdriver.Chrome(options=option)
# driver.maximize_window()  # 设置页面最大化，避免元素被隐藏
# url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# driver.get(url)
# driver.switch_to.frame('iframeResult')
# source = driver.find_element(By.CSS_SELECTOR,'#draggable')
# target = driver.find_element(By.CSS_SELECTOR,'#droppable')
# actions = ActionChains(driver)
# actions.drag_and_drop(source=source, target=target)
# actions.perform()


##############3 执行JavaScript
######知乎进度条下拉
# from selenium import webdriver

# option = webdriver.ChromeOptions()
# option.add_experimental_option("detach", True)
# driver = webdriver.Chrome(option)
# driver.get('https://www.zhihu.com/explore')
# driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# driver.execute_script('alert("To Bottom")')

################ 获取元素信息
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By

# option = webdriver.ChromeOptions()
# option.add_experimental_option('detach',True)
# driver = webdriver.Chrome(option)
# driver.get('https://www.zhihu.com/explore')
# logo = driver.find_element(By.CLASS_NAME,'ExploreHomePage-specialsLoginImg')
# print(logo)
# print(logo.get_attribute('class'))
# input = driver.find_element(By.CLASS_NAME,'ExploreHomePage-specialsLoginTitle')
# print(input.text)
# print(input.id)
# print(input.location)
# print(input.size)

################## Frame
# import time
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.by import By

# option = webdriver.ChromeOptions()
# option.add_experimental_option('detach',True)
# driver = webdriver.Chrome(option)
# url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# driver.get(url)
# driver.switch_to.frame('iframeResult')
# source = driver.find_element(By.CSS_SELECTOR,'#draggable')
# # target = driver.find_element(By.CSS_SELECTOR,'#droppable')
# print(source)
# try:
#     logo = driver.find_element(By.CLASS_NAME,'logo')
# except:
#     print('No logo')
# driver.switch_to.parent_frame()
# logo = driver.find_element(By.CLASS_NAME,'logo')
# print(logo)
# print(logo.text)

################## 等待
######## 隐式等待
#### 当使用隐式等待执行测试的时候，如果WebDriver再没有DOM中找到元素，将继续等待，超出设定时间后抛出找不到元素的异常。
#### 也就是，当查找的元素并没有立即出现的时候，隐式等待将等待一段时间再查找DOM，默认时间是0
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.get("https://www.baidu.com")
# input = driver.find_element(By.ID,'kw')
# print(input)


####### 显式等待
# 原理：显示等待，就是明确的要等到某个元素的出现或者是某个元素的可点击等条件，等不到，就一直等，除非在规定的时间之内都没找到，那么久跳出Exception
# (简而言之，就是直到元素出现才去操作，如果超时则报异常)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# driver.get('https://www.taobao.com/')
# wait = WebDriverWait(driver,0)
# input = wait.until(EC.presence_of_element_located((By.ID,'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))
# print(input,button)

##########################前进后退
# import time
# from selenium import webdriver

# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# driver.get('https://www.taobao.com')
# driver.get('https://www.python.org')
# driver.back()
# time.sleep(5)
# driver.forward()

#####################3 Cookies
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('https://www.zhihu.com/explore')
# driver.maximize_window() # driver.maximize_window()  # 设置页面最大化，避免元素被隐藏
# print(driver.get_cookies())
# driver.delete_all_cookies()
# driver.add_cookie({'name':'name','domain':'www.zhihu.com','value':'germey'})
# print(driver.get_cookies())
######################## 选项卡管理
# import time
# from selenium import webdriver
# option = webdriver.ChromeOptions()

# option.add_experimental_option('detach',True)
# driver = webdriver.Chrome(options=option)
# driver.get('https://www.baidu.com')
# driver.execute_script('window.open()')
# print(driver.window_handles)
# driver.switch_to.window(driver.window_handles[1])
# driver.get('https://www.taobao.com')
# time.sleep(3)
# driver.switch_to.window(driver.window_handles[0])
# driver.get('https://python.org')

####################异常处理

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException

# driver = webdriver.Chrome()
# driver.get('https://baidu.com')
# try:
#     driver.find_element(By.ID,'Hello')
# except NoSuchElementException:
#     print('No Element')
# finally:
#     driver.close()

# try:
#     driver.get('http://www.baidu.com')
#     input = driver.find_element(By.ID, 'kw')
#     driver.implicitly_wait(10)
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(driver,10)
#     wait.until(EC.presence_of_element_located((By.ID,"content_left")))
#     print(driver.current_url)
#     print(driver.get_cookies())
#     print(driver.page_source)
# finally:
#     driver.close()

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