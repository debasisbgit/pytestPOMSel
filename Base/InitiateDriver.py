from _tracemalloc import start

from selenium import webdriver
from Library import ConfigReader


def startBrowser():
    print("inside startbrowser")
    global driver
    path = "F:/_Python_Selenium_Program_2020/bwdrv/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=path)
    driver.get('https://www.google.com/')
    driver.maximize_window()
    #driver.find_element_by_css_selector("#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input").send_keys("rediff")

    #driver.find_element_by_css_selector().send_keys()
    #driver.find_element_by_css_selector("").click()
    #print(driver.title)
    return driver


def closeBrowser():
    print("inside close bw")
    driver.close()

