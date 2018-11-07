from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Google():

    def googleSearch(self):

        driver = webdriver.Firefox()

        driver.maximize_window()
        driver.implicitly_wait(3)

        driver.get('https://www.google.com/')

        search = driver.find_element(By.XPATH,"//input[@title='Search']")
        search.send_keys('Hello')
        search.click()
        searchbtn = driver.find_element(By.XPATH,"//input[@value='Google Search'][1]")
        searchbtn.click()

c= Google()

c.googleSearch()
