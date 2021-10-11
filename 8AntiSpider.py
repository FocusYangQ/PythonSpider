import requests

# 绕过反爬机制，就是设置header
if __name__ == "__main__" :

    response = requests.get ( "http://www.zhihu.com" )
    print ( "第一次,不设头部信息,状态码:" , end = "" )
    print ( response.status_code ) # 不写头部，返回403，不能正常爬取

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }

    response = requests.get ( "http://www.zhihu.com" , headers = headers )
    print ( response.status_code )
    print ( response.text )