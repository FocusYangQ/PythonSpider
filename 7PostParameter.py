import requests

if __name__ == '__main__' :

    data = {
        "name" : "hezhi" ,
        "age" : 20
    }

    response = requests.post ( "http://httpbin.org/post" , params = data )

    print ( response.status_code )
    print ( response.text )