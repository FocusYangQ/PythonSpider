# BeautifulSoup 网页源码解析器
# import bs4
# 用来代替 bs4 中解析器的一部分
# import lxml
# 正则的优点： 1、速度快 2、能够提取某些解析器提取不到的数据
# 正则的缺点： 1、不直观

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__' :

    response = requests.get ( 'https://www.baidu.com' )
    print ( response ) # 打印请求结果的状态码
    print ( response.content ) #打印请求到的网页源码

    # 将网页源码构造成 BeautifulSoup 对象
    bsobj = BeautifulSoup ( response.content , 'lxml' )
    # 获取网页中所有 a 标签对象
    a_list = bsobj.find_all ( 'a' )
    text = ''
    for a in a_list :
        # 打印a标签对象的 href 属性，即这个对象指向的链接地址
        print ( a.get ( 'href' ) )
        href = a.get ( 'href' )
        text += href + '\n'
    # with …… as …… 来打开文件，在操作完成后，会自动关闭文件
    with open ( 'url.txt' , 'w' ) as file :
        file.write ( text )
