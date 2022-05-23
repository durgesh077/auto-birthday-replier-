from selenium import webdriver
from random import *
import time
import os
from selenium.webdriver.common.keys import Keys
from func import *
def starter():
    driver = webdriver.Chrome(executable_path=r'C:\Program Files\chromedriverer\chromedriver.exe')
    driver.maximize_window()
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    driver.get("https://web.whatsapp.com")
    while len(driver.find_elements_by_css_selector(".cbRtt")):
        #print("scan...")
        time.sleep(5)
    driver.find_element_by_css_selector("[type='checkbox']").click()
    while True:
        checkMessage(driver)
        sleep(4)
        driver.find_element_by_css_selector('[title="CS official"]').click()
    return

starter()

