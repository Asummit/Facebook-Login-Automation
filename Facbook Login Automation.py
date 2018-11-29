#Import Selenium python library..
from selenium import webdriver
driver = webdriver.Chrome(executable_path=r'C:\Users\samola\Desktop\chromedriver') #path for your chromedriver
driver.get('https://www.facebook.com/')
xpath1 = '//*[@id="email"]'
box1 = driver.find_element_by_xpath(xpath1)
box1.send_keys('*Your User_ID*')
xpath2 = '//*[@id="pass"]'
box2 = driver.find_element_by_xpath(xpath2)
box2.send_keys('*Your Password*')
box2.submit()
