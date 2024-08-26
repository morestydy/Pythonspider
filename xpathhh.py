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


# from lxml import etree

# html = etree.HTML(text)

# result0 = html.xpath('//ul/li/a/text()')

# print(result0)


import requests
import re
import pandas as pd
from lxml import etree

url = 'https://pic.netbian.com/new/index_.html'
for page in range(20):
    
