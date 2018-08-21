from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import time
import urllib
import urllib3
import fangfa as ff
import exceltojson as e_to_j
import personData
import setting



#构造模拟浏览器

p1 = personData.personData("欧金珍","432424194312161827","18673669254","6217995580013941192","蒋娟")
my= setting.setting()

chromedriver = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver"

os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver) #模拟打开浏览器

driver.implicitly_wait(10)  

url = "http://cpadisc4.cpad.gov.cn/cpad/login"

driver.get(url) #打开网址

driver.maximize_window() #窗口最大化
#time.sleep(8) #等待网页加载20秒

#！！尚未加载 异常处理

# driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click() #点击登录按钮

#time.sleep(2)
#driver.find_element_by_class_name('ng-pristine ng-invalid ui-inputtext ui-corner-all ui-state-default ui-widget ng-touched').clear() #先清除输入框内容
#driver.find_element_by_xpath("//input[@formcontrolname='account']").send_keys(u'43072320801') #输入账号








driver.find_element_by_xpath(my.xpath1).send_keys(my.account) #输入账号

#time.sleep(1)

driver.find_element_by_xpath(my.xpath2).send_keys(my.password) #输入密码

yanzhengma = input("请手动输入验证码：")
driver.find_element_by_xpath(my.xpath3).send_keys(yanzhengma) #输入密码
#time.sleep(1)
driver.find_element_by_xpath(my.xpath4).click()
#登陆成功

#加载时间过长  异常处理

time.sleep(2)
driver.find_element_by_xpath(my.xpath5).click()
time.sleep(1)
driver.find_element_by_xpath(my.xpath6).click()
time.sleep(1)
driver.find_element_by_xpath(my.xpath7).click()
time.sleep(1)
driver.find_element_by_xpath(my.xpath8).click()   #点击贫困户维护页面
#time.sleep(5)

#显示查询画面
#driver.find_element_by_xpath("//input[@formcontrolname='aab002']").send_keys(u'张梅') #输入查询人姓名
#time.sleep(2)
#！！出现重名，所以弃用

driver.find_element_by_xpath(my.xpath9).send_keys(p1.ID) #输入查询人身份证号
time.sleep(1)
driver.find_element_by_xpath(my.xpath10).click() #点击查询按钮

time.sleep(0.5)

#！！如果查询不到  异常处理   记录日志    保存日志

#driver.find_element_by_xpath("//*[@id="ui-tabpanel-1"]/div/busi-tab/object-poor-family/p-panel[3]/div/div[2]/div/div/object-poor-family-grid/p-datatable/div/div[1]/div/div[2]/div/table/tbody/tr/td[4]/span/span").click() #点击第一栏查询项姓名栏（如果查询结果唯一）
#time.sleep(2)

driver.find_element_by_xpath(my.xpath11).click() #点击第一栏查询项姓名栏（如果查询结果唯一）
time.sleep(0.5)

driver.find_element_by_xpath(my.xpath12).clear()
driver.find_element_by_xpath(my.xpath12).send_keys(p1.phone)
time.sleep(0.5)

#formcontrolname="aar012" 联系电话
driver.find_element_by_xpath(my.xpath13).clear()
driver.find_element_by_xpath(my.xpath13).send_keys(p1.cardnumber)
time.sleep(0.5)

#formcontrolname="aac004" 银行卡号

driver.find_element_by_xpath(my.xpath14).click() #点击帮扶责任人结对信息栏
time.sleep(2)

try:#判定是否发现该结对帮扶人
    driver.find_element_by_xpath("//span[contains(.,%s)]"% p1.name)
    a=True
except:
    a=False


if a:#如果新增结对帮扶人与现存结对帮扶人相同，选择修改日期选项
 
    ##//span[contains(.,'蒋娟')]/../../td/p-dtradiobutton/div/div/input
    #radio1 = driver.find_element_by_xpath("//span[contains(.,%s)]/../../td/p-dtradiobutton/div/div/input"% p1.name)
    ##js = 'document.querySelectorAll("input")[0].style.display="block";' 
    #driver.execute_script('arguments[0].removeAttribute(\"style\")',radio1) 


    


    #chain = ActionChains(driver)
    #implement = driver.find_element_by_xpath("//span[contains(.,%s)]/../../td/p-dtradiobutton/div/div[2]/span"% p1.name)
    #chain.move_to_element(implement).perform()#鼠标悬停
    #time.sleep(2)

    #driver.find_element_by_xpath("//span[contains(.,%s)]/../../td/p-dtradiobutton/div/div/input"% p1.name).click()#点击与现存结对帮扶人姓名对应的单选框，然后修改日期

    driver.find_element_by_xpath(my.xpath17).click()#修改日期
    driver.find_element_by_xpath(my.xpath18).send_keys(p1.startdate)
    driver.find_element_by_xpath(my.xpath19).send_keys(p1.enddate)
    driver.find_element_by_xpath(my.xpath20).click()#点击保存
    time.sleep(0.5)
    driver.find_element_by_xpath(my.xpath26).click()#点击确定
else:#否则点击新增结对帮扶人
    driver.find_element_by_xpath(my.xpath16).click()#新增结对
    driver.find_element_by_xpath(my.xpath21).send_keys(p1.helpPerson)#输入结对帮扶人姓名
    driver.find_element_by_xpath(my.xpath22).click()#点击查询
    driver.find_element_by_xpath(my.xpath24).send_keys(p1.startdate)
    driver.find_element_by_xpath(my.xpath25).send_keys(p1.enddate)
    driver.find_element_by_xpath(my.xpath23).click()#点击保存
    time.sleep(0.5)
    driver.find_element_by_xpath(my.xpath26).click()#点击确定
    time.sleep(0.5)

driver.find_element_by_xpath(my.xpath27).click()#点击页面保存
time.sleep(0.5)
driver.find_element_by_xpath(my.xpath26).click()#点击确定
time.sleep(0.5)
driver.find_element_by_xpath(my.xpath28).click()#关闭弹出页面
time.sleep(0.5)






    






#driver.find_element_by_xpath("//*[@id="ui-tabpanel-1"]/div/busi-tab/object-poor-family/p-panel[3]/div/div[2]/div/div/object-poor-family-grid/p-datatable/div/div[1]/div/div[2]/div/table/tbody/tr[1]/td[4]/span/span/a").click()#点击第一栏查询项姓名栏（如果查询结果不唯一）
#time.sleep(2)

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


#e_to_j.excel_json(r"C:\Users\wangz\Desktop\东岳村 贫困户信息_20180814.xlsx",r"C:\Users\wangz\Desktop\2.json")   #转换








