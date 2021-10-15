from time import sleep

from selenium import webdriver

if __name__ == '__main__':

    driver = webdriver.Chrome()
    print(driver.current_url)

    # driver= webdriver.Chrome() #  需要 下载 对应浏览器 驱动到 python 安装目录
    # driver.get("http://210.40.3.30/redir.php?catalog_id=121&object_id=2737") # 刷新网址
    #
    # for i in range(10000): # 刷新次数
    #     driver.refresh()  # 刷新网页
    #     sleep ( 0.5 ) # 五秒一次
    #     print ( i )