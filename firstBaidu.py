import requests #导入爬虫的库

#爬取强大的BD页面，打印页面信息
if __name__ == '__main__':

    response = requests.get ( "http://www.baidu.com" )   #生成一个response对象
    response.encoding = response.apparent_encoding #设置编码格式
    print ( "状态码：" + str ( response.status_code ) )
    print ( response.text )