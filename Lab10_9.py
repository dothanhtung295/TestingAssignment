import time
from selenium import webdriver
driver = webdriver.Chrome('D:\ki2nam3\KiemThuPhanMem\Chrome_Driver\chromedriver.exe')
driver.maximize_window()
driver.get('https://itmscoaching.herokuapp.com/form')
title1 = driver.title
assert title1 == "Formy"
first_name = driver.find_element_by_id('first-name')
first_name.send_keys('Binh')
last_name = driver.find_element_by_id('last-name')
last_name.send_keys('Nguyen')
job_title = driver.find_element_by_id('job-title')
job_title.send_keys('Tester')
grad_sc = driver.find_element_by_xpath('//*[@id="radio-button-3"]')
grad_sc.click()
sex = driver.find_element_by_xpath('//*[@id="checkbox-2"]')
sex.click()
yoe = driver.find_element_by_xpath('//*[@id="select-menu"]/option[4]')
yoe.click()
date = driver.find_element_by_id('datepicker')
date.send_keys('07/20/2011')
time.sleep(2)
btn_submit = driver.find_element_by_css_selector("[class ='btn btn-lg btn-primary']")
btn_submit.click()
title2 = driver.title
assert title2 == "Formy"
time.sleep(2)
driver.close()
