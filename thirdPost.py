from urllib import response

import requests #导入爬虫的库

if __name__ == '__main__' :

    response = requests.post ( "http://httpbin.org/post" )
    print ( response.status_code )
    print ( response.text )