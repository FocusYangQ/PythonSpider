import requests

if __name__ == '__main__' :

    response = requests.get ( "http://httpbin.org/get?name=hezhi&age=20" )
    print ( response.status_code )
    print ( response.text )