from pyquery import PyQuery as pq

# 字符串初始化
html = '''
    <div>",
        <ul>",
             <li class=\"item-0\">first item</li>",
             <li class=\"item-1\"><a href=\"link2.html\">second item</a></li>",
             <li class=\"item-0 active\"><a href=\"link3.html\"><span class=\"bold\">third item</span></a></li>",
             <li class=\"item-1 active\"><a href=\"link4.html\">fourth item</a></li>",
             <li class=\"item-0\"><a href=\"link5.html\">fifth item</a></li>",
         </ul>,
     </div>,
    '''
# doc = pq(html)
# print(doc('li'))
# url初始化
doc = pq(url='https://baidu.com')
# print(doc('head'))

# 文件初始化
doc = pq(filename = 'test.html')
# print(doc('li'))
# 基本CSS选择器
#### id使用#号,class前加.,标签不加
html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
doc = pq(html)
# print(doc('#container .list li'))

# 查找元素
# item = doc('.list')
# print(type(item))
# print(item)
# print(item.find('li')('.item-0'))

li = doc('.item-0.active')
# print(li)

# lis = doc('li').items()
# for li in lis:
#     print(li)

############################# 获取信息
################ 获取属性
a = doc('.item-0.active a')
# print(a)
# print(a.attr.href)
# print(a.attr('href'))
######################### 获取文本
# print(a.text())
####################  获取html
# print(a.html())