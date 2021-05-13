import time
from selenium import webdriver
driver = webdriver.Chrome('D:\ki2nam3\KiemThuPhanMem\Chrome_Driver\chromedriver.exe')
driver.maximize_window()
driver.get('http://practice.automationtesting.in/')
title1 = driver.title
assert title1 == "Automation Practice Site"
next1 = driver.find_element_by_xpath('//*[@id="menu-item-50"]/a')
asnext1 = next1.text
assert asnext1 == "My Account"
next1.click()
title2 = driver.title
assert title2 == "My Account – Automation Practice Site"
email_reg = driver.find_element_by_id('reg_email')
email_reg.send_keys('a123@gmail.com')
pass_reg = driver.find_element_by_id('reg_password')
as_pass = pass_reg.text
print(as_pass)
pass_reg.send_keys('123abc')
btn_reg = driver.find_element_by_name('register')
as_btn = btn_reg.text
print(as_btn)
btn_reg.submit()
time.sleep(2)
driver.quit()