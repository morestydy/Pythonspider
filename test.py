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


import pandas as pd
import requests
from fake_useragent import UserAgent
import time
import re

# url = 'https://www.maoyan.com/board/4?offset=10'
# headers = {'User-Agent':UserAgent().random}
# response = requests.get(url=url,headers=headers)
# response.raise_for_status()
# response.encoding = response.apparent_encoding
# print(response.status_code)
# print(response.url)
# with open('maoyan.txt','w',encoding='utf-8') as f:
#     f.write(response.text)
########################################猫眼#################
movies_date = pd.DataFrame(columns=['title','stars','releasetime','score','link'])
headers = {'User-Agent':UserAgent().random}
with open('maoyan.txt','r',encoding='utf-8') as f:
    html = f.read()
    movie_list = re.findall('<dd>.*?<img data-src="(.*?)".*?<p class="name">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">上映时间：(.*?)</p>.*?<p class="score"><i class="integer">(.*?)</i><i class="fraction">(.*?)</i></p>.*?</dd>',html,re.S)
    # print(movie_list)
    for link,title,stars,releasetime,integer,fraction in movie_list:
        # print(f'link:{link},title:{title},stars:{stars},releasetime:{releasetime},score:{integer}{fraction}')
        mov_record={
            'title':title.replace('主演：',''),
            'stars':stars.strip(),
            'releasetime':releasetime,
            'score':integer+fraction,
            'link':link.strip()
        }
        # img_content = requests.get(link,headers=headers).content
        # with open(f'maoyan\\{title}.jpg','wb') as f:
        #     f.write(img_content)
        print(mov_record['title'])
#         movies_date=movies_date._append(mov_record,ignore_index=True)
# movies_date.to_excel('douban.xlsx',index=False)



# import json
# import requests
# from requests.exceptions import RequestException
# import re
# import time


# def get_one_page(url):
#     try:
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
#         }
#         response = requests.get(url, headers=headers)
#         if response.status_code == 200:
#             return response.text
#         return None
#     except RequestException:
#         return None


# def parse_one_page(html):
#     pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
#                          + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
#                          + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
#     items = re.findall(pattern, html)
#     for item in items:
#         yield {
#             'index': item[0],
#             'image': item[1],
#             'title': item[2],
#             'actor': item[3].strip()[3:],
#             'time': item[4].strip()[5:],
#             'score': item[5] + item[6]
#         }


# def write_to_file(content):
#     with open('result.txt', 'a', encoding='utf-8') as f:
#         f.write(json.dumps(content, ensure_ascii=False) + '\n')


# def main(offset):
#     url = 'http://maoyan.com/board/4?offset=' + str(offset)
#     html = get_one_page(url)
#     for item in parse_one_page(html):
#         print(item)
#         write_to_file(item)


# if __name__ == '__main__':
#     for i in range(10):
#         main(offset=i * 10)
#         time.sleep(1)