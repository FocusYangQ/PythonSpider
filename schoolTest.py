import requests

if __name__ == '__main__' :

    response = requests.get("http://210.40.3.30/redir.php?catalog_id=121&object_id=2737")

    # i = 1
    # while i < 10000 :
    #     response = requests.get("http://210.40.3.30/redir.php?catalog_id=121&object_id=2737")
    #     i += 1
    #     print ( i )
