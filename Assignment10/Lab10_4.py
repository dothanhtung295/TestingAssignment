import time
from selenium import webdriver
driver = webdriver.Chrome('D:\ki2nam3\KiemThuPhanMem\Chrome_Driver\chromedriver.exe')
driver.maximize_window()
driver.get('http://practice.automationtesting.in/')
title = driver.title
assert title == "Automation Practice Site"
time.sleep(2)
driver.quit()