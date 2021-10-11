import requests

if __name__ == '__main__' :

    response = requests.get ( "https://www.baidu.com/img/baidu_jgylogo3.gif" )

    # 打开一个文件夹， wb 表示以二进制格式打开一个文件只用于写入
    file = open ( "G:\\PythonProjectTest\\baidu_logo.gif" , "wb" )

    file.write ( response.content )

    file.close ()