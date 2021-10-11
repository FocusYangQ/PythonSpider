import requests

if __name__ == '__main__' :

    response = requests.put ( "http://httpbin.org/put" )
    print ( response.status_code )
    print ( response.text )
