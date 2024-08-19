# 2. 爬虫https://www.maoyan.com/board/,图片 标题 分数
import pandas as pd
import requests
from fake_useragent import UserAgent
import re
import time

movies_date = pd.DataFrame(columns=['title','stars','releasetime','score','link'])
headers = {'User-Agent':UserAgent().random}
cooks = {'Cookie':'__mta=20780679.1723882575956.1724067820086.1724068145043.11; uuid_n_v=v1; uuid=F91D3C305C7011EF8BA6E5594D7FF2C37772D15118EE4514B0E77F0E70442629; _lxsdk_cuid=1915f689732c8-0e8bccadec96ba-4c657b58-1bcab9-1915f689732c8; _lxsdk=F91D3C305C7011EF8BA6E5594D7FF2C37772D15118EE4514B0E77F0E70442629; _csrf=8b6499d94bd946fde3698de0763e03c085b3168ee05703538f4cf50cecd5d513; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1723882576,1724050716; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1724050716; HMACCOUNT=EFA24E3BB02D39F1; _lxsdk_s=1916a7331f0-71e-f7c-06f%7C%7C3'}
for page in range(10):
    url = 'https://www.maoyan.com/board/4?offset='+str(page*10)
    print(url)
    response = requests.get(url=url,headers=headers,cookies=cooks)
    response.raise_for_status()
    response.encoding = response.apparent_encoding
    movie_list = re.findall('<dd>.*?<img data-src="(.*?)".*?<p class="name">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">上映时间：(.*?)</p>.*?<p class="score"><i class="integer">(.*?)</i><i class="fraction">(.*?)</i></p>.*?</dd>',response.text,re.S)
    for link,title,stars,releasetime,integer,fraction in movie_list:
        # print(f'link:{link},title:{title},stars:{stars},releasetime:{releasetime},score:{integer}{fraction}')
        mov_record={
            'title':title.replace('主演：',''),
            'stars':stars.strip(),
            'releasetime':releasetime,
            'score':integer+fraction,
            'link':link.strip()
        }
        print(title)
        img_content = requests.get(link,headers=headers,cookies=cooks).content
        with open(f'maoyan\\{title}.jpg','wb') as f:
            f.write(img_content)
            print(f'写入图片:{title}')
        movies_date=movies_date._append(mov_record,ignore_index=True)
    time.sleep(2)
movies_date.to_excel('maoyan.xlsx',index=False)



