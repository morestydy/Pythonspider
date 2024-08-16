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
import requests
from fake_useragent import UserAgent
import pandas as pd
import re



# movies=pd.DataFrame(columns=['title','score','link'])
movies_data=pd.DataFrame(columns=['title','score','link'])
# movie_record = {}
for pages in range(1,4):
    headers = {
        'UserAgent':UserAgent().random
    }
    url=r'https://ssr1.scrape.center/page/'+str(pages)
    response = requests.get(url,headers=headers)
    response.raise_for_status()
    response.encoding = response.apparent_encoding
    # print(response.status_code)
    title_list = re.findall(r'<a data-v-7f856186.*?src="(.*?.jpg)@.*?cover">.*?class="m-b-sm">(.*?)</h2>.*?<p.*?score.*?>(.*?)</p>',response.text,re.S)
    # print(title_list)
    for link,title,score in title_list:
        safe_title = re.sub(r'[<>:"/\\|?*\x00-\x1F]', '', title)
        print(f'pic:{link},title:{safe_title},score:{score}')
        # 图片下载
        # img_content = requests.get(link,headers=headers).content
        # with open(f'pic\\{safe_title}.jpg',mode='wb') as f:
        #     f.write(img_content)
        movie_record = {
            'title': safe_title,
            'score': score.strip(),
            'link': link.strip()
        }
        movies_data = movies_data._append(movie_record,ignore_index=True)
movies_data.to_excel('movies.xlsx', index=False)