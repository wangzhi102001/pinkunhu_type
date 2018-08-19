from selenium import webdriver
import os
import time
import urllib
import urllib3
import fangfa as ff



#构造模拟浏览器

chromedriver = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver"

os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver) #模拟打开浏览器

time.sleep(2)

url = "http://cpadisc4.cpad.gov.cn/cpad/login"

driver.get(url) #打开网址

driver.maximize_window() #窗口最大化
time.sleep(8) #等待网页加载20秒

# driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click() #点击登录按钮

time.sleep(2)
#driver.find_element_by_class_name('ng-pristine ng-invalid ui-inputtext ui-corner-all ui-state-default ui-widget ng-touched').clear() #先清除输入框内容
driver.find_element_by_xpath("//input[@formcontrolname='account']").send_keys(u'43072320801') #输入账号

time.sleep(1)

driver.find_element_by_xpath("//input[@formcontrolname='password']").send_keys(u'000724') #输入密码

yanzhengma = input("请手动输入验证码：")
driver.find_element_by_xpath("//input[@formcontrolname='inputCode']").send_keys(yanzhengma) #输入密码
time.sleep(1)
driver.find_element_by_xpath("//span[@class='ui-button-text ui-clickable']").click()
