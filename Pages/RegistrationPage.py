from Library import ConfigReader
from Library import ConfigReader
import time
from selenium import webdriver


class registrationclass:
    def __init__(self, obj):
        global dri
        dri = obj

    def enter_kwsearch(self):
        #path = "F:/_Python_Selenium_Program_2020/bwdrv/chromedriver.exe"
        #driver = webdriver.Chrome(executable_path=path)
        # driver.get('https://www.google.com/')
        # driver.find_element_by_css_selector("#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input").send_keys("rediff")
        #driver.get('https://www.google.com/')
        #driver.find_element_by_css_selector("#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input").send_keys("rediff")
        #dri.get('https://www.google.com/')
        dri.find_element_by_css_selector\
            ("#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input").send_keys("taj mahal")

        #dri.find_element_by_css_selector(" # lga").click()
        #dri.find_element_by_css_selector("# tsf > div:nth-child(2) > div.A8SBwf > div.FPdoLc.tfB0Bf > center > input.gNO89b").click()




