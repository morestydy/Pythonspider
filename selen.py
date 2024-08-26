from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json
import os
import urllib
import ssl
import urllib.request

# 创建一个未验证的上下文，避免SSL证书的问题
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
# 加载谷歌浏览器驱动
driver_path = r'C:\\Program Files\\Google\Chrome\\Application\\'
ser = Service(driver_path)
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=chrome_options)
driver.maximize_window()  # 设置页面最大化，避免元素被隐藏

def get_link(url, i):
    url = f"{url}/page{i}"
    print(f"开始第{i}页")
    driver.get(url)  # 打开目标页面

    while True:
     # 滑动到最底部，加载出所有图片
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        # 检测是不是到最底部了
        if driver.execute_script("return window.innerHeight + window.pageYOffset >= document.body.offsetHeight;"):
            break

# 要获取的页面链接
url = "https://flickr.com/photos/coloraestheticist"
# 页面总数
n = 2
for i in range(1, n+1):
    get_link(i)
    links = [i.get_attribute("href") for i in driver.find_elements(By.CLASS_NAME, 'overlay')]
    print(f"第{i}页，图片：{len(links)}张")
    with open(f"downloaded_images/links/{i}.txt", "w") as file:
        for link in links:
            file.write(link + "\n")

link = "https://flickr.com/photos/coloraestheticist/53898259811/"
driver.get(link) 

def get_element(endswith, click=False):
    '''
    点击下载/获取图片链接
    '''
    # 获取所有符合条件的元素
    elements = driver.find_elements(By.XPATH, '//a[starts-with(@id, "yui_3_16_0")]')

    # 遍历元素并打印它们的 href 属性值
    for element in elements:
        href = element.get_attribute('href')
        if href.endswith(endswith):
            if click:
                element.click()
            else:
                return href
            


def download_imgs(links, save_directory):
    global driver
    for link in links:
        max_retries = 3
        for retry in range(max_retries):
            try:
                driver.get(link+"sizes/o/")
                time.sleep(1)
                image_url = driver.find_element(By.XPATH, '//*[@id="allsizes-photo"]/img').get_attribute("src")
                if image_url:
                    break
            except Exception as e:
                print(f"获取失败：{e}")
        if not image_url:
            print(f"【图片获取失败】{link}")
            return 
        image_filename = image_url.split("/")[-1]
        print(f"正在下载：{image_filename}")
        save_path = os.path.join(save_directory, image_filename)

        for retry in range(max_retries):
            try:
                response = urllib.request.urlopen(image_url, context=context, timeout=3)
                if response.status == 200:
                    break
            except Exception as e:
                print(f"请求失败：{e}")

        image_data = response.read()
        with open(save_path, "wb") as file:
            file.write(image_data)
        time.sleep(1)


def batch_download_images_from_files(links_directory, output_directory):
    # 确保输出目录存在
    os.makedirs(output_directory, exist_ok=True)
    
    # 遍历所有的链接文件
    for file_name in os.listdir(links_directory):
        file_path = os.path.join(links_directory, file_name)
        
        # 读取链接文件中的所有图片链接
        with open(file_path, 'r') as file:
            links = file.readlines()
        
        # 从链接中去掉换行符
        links = [link.strip() for link in links]
        
        # 为每个链接调用 download_imgs 函数下载图片
        print(f"开始下载 {file_name} 中的图片...")
        download_imgs(links, output_directory)
        print(f"{file_name} 中的图片下载完成!")

# 定义链接文件所在目录和图片保存目录
links_directory = "downloaded_images/links"
output_directory = "downloaded_images/imgs"

# 执行批量下载
batch_download_images_from_files(links_directory, output_directory)