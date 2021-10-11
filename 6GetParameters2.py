import requests

if __name__ == '__main__' :

    data = {
        "name" : "hezhi" ,
        "age" : 20
    }

    response = requests.get ( "http://httpbin.org/get" , params = data )

    print ( response.status_code )
    print ( response.text )