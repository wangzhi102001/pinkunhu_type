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

#！！尚未加载 异常处理

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
#登陆成功

#加载时间过长  异常处理

time.sleep(5)
driver.find_element_by_xpath("//a[@title='扶贫对象']").click()
time.sleep(2)
driver.find_element_by_xpath("//a[@title='基础信息维护']").click()
time.sleep(2)
driver.find_element_by_xpath("//a[@title='2018年度']").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/app-root/div/div/app-main-layout/div/div[1]/div/div/app-menu/ul/nui-main-menu/div/div[1]/div[2]/div/nui-main-menu-sub/ul/li/nui-main-menu-sub/ul/li[6]/nui-main-menu-sub/ul/li[1]/a/span[2]").click()   #点击贫困户维护页面
time.sleep(5)

#显示查询画面
#driver.find_element_by_xpath("//input[@formcontrolname='aab002']").send_keys(u'张梅') #输入查询人姓名
#time.sleep(2)
#！！出现重名，所以弃用

driver.find_element_by_xpath("//input[@formcontrolname='aab004']").send_keys(u'43072319830810522062') #输入查询人身份证号
time.sleep(2)
driver.find_element_by_xpath("//button[@label='查询']/span").click() #点击查询按钮

time.sleep(2)

#！！如果查询不到  异常处理   记录日志    保存日志

#driver.find_element_by_xpath("//*[@id="ui-tabpanel-1"]/div/busi-tab/object-poor-family/p-panel[3]/div/div[2]/div/div/object-poor-family-grid/p-datatable/div/div[1]/div/div[2]/div/table/tbody/tr/td[4]/span/span").click() #点击第一栏查询项姓名栏（如果查询结果唯一）
#time.sleep(2)

driver.find_element_by_xpath("//tbody[@class='ui-datatable-data ui-widget-content ui-datatable-hoverable-rows']/tr/td[4]").click() #点击第一栏查询项姓名栏（如果查询结果唯一）
time.sleep(2)
driver.find_element_by_xpath("//span[contains(text(),'五、帮扶责任人结对信息')]").click() #点击帮扶责任人结对信息栏
time.sleep(2)

#driver.find_element_by_xpath("//*[@id="ui-tabpanel-1"]/div/busi-tab/object-poor-family/p-panel[3]/div/div[2]/div/div/object-poor-family-grid/p-datatable/div/div[1]/div/div[2]/div/table/tbody/tr[1]/td[4]/span/span/a").click()#点击第一栏查询项姓名栏（如果查询结果不唯一）
#time.sleep(2)

#formcontrolname="aar012" 联系电话
#formcontrolname="aac004" 银行卡号

#xpath（//span[contains(text(),'五、帮扶责任人结对信息')]）

#  //button[@label='取消结对']/span
#  //button[@label='增加结对']/span
#  //button[@label='修改时间']/span

#修改日期   1.开始日期  label   //input[@class='ng-tns-c6-73 ui-inputtext ui-widget ui-state-default ui-corner-all']
#          2.结束日期  label    //input[@class='ng-tns-c6-74 ui-inputtext ui-widget ui-state-default ui-corner-all']
#          3.保存修改日期   button   //button[@id = 'saveTime' and @label='保存']

#新增结对帮扶人姓名  1.输入结对帮扶人姓名  //input[@formcontrolname='aab002']
#                   2.查询   button   //button[@id = 'queryByName' and @label='查询']
#                   3.开始日期   //input[@class='ng-tns-c6-71 ui-inputtext ui-widget ui-state-default ui-corner-all']
#                   4.结束日期   //input[@class='ng-tns-c6-72 ui-inputtext ui-widget ui-state-default ui-corner-all']
#  如果查询无结果  异常处理



#  整体确定     1.button   //button[@class='swal2-confirm swal2-styled']

###


###   excel转json

###  循环体   











