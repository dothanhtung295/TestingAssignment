from selenium import webdriver
import time
driver = webdriver.Chrome('D:\ki2nam3\KiemThuPhanMem\Chrome_Driver\chromedriver.exe')
driver.set_window_position(0, 0)
driver.set_window_size(800, 800)
driver.get('http://practice.automationtesting.in/')
title = driver.title
assert title == "Automation Practice Site"
time.sleep(2)
driver.quit()