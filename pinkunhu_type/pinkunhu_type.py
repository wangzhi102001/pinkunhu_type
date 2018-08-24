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
import json
import sys
from selenium.common.exceptions import ElementNotVisibleException,NoSuchElementException,TimeoutException


#读取json数据库,获取待处理列表

list_poor_family_js=[]#所有待处理的贫困户数据JS类型

list_poor_family=[]#所有待处理的贫困户数据
personDatas =[]
n =0 #计数器
end = 0
start = 0
error = 0
switch_1=True
error_count =0

while True:
    print('''
    准备工作:请将与Chrome浏览器版本对应的chromedriver，并放在Chrome程序目录Application文件夹中；
    1.第一次运行：请按照excel模板在目录下放入excel文件，并命名为"001.xlsx",后再输入1后回车，;
    2.非首次运行，请确保上次保存的"002.json"存在后，输入2，回车后，开始加载进度。
    3.输入q/Q退出。
    ''')
    input_num=input()
    if input_num=="1":
        e_to_j.excel_json('001.xlsx'or'001.xls','001.json')
        e_to_j.file_to_json_fomat("001.json","002.json",personDatas,list_poor_family)
        e_to_j.json_to_personDatalist("002.json",list_poor_family_js,list_poor_family,error,start,end,n)
        break
    
    elif input_num=="2":
        e_to_j.json_to_personDatalist("002.json",list_poor_family_js,list_poor_family,error,start,end,n)
        break
    #elif str(input_num).lower=='q':
    #    sys.exit()
    
    else:
        print("请重新输入")
#input()


e_to_j.personDatalist_to_json(list_poor_family,'002.json')

#初始化---------
#input()
#e_to_j.save_as_json(list_poor_family,'002.json')

#构造模拟浏览器

my= setting.setting()

chromedriver = my.chromePath

os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver) #模拟打开浏览器

driver.implicitly_wait(3)  

url = my.url

driver.get(url) #打开网址

driver.maximize_window() #窗口最大化
#time.sleep(8) #等待网页加载20秒

#！！尚未加载 异常处理

# driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click() #点击登录按钮

#time.sleep(2)
#driver.find_element_by_class_name('ng-pristine ng-invalid ui-inputtext ui-corner-all ui-state-default ui-widget ng-touched').clear() #先清除输入框内容
#driver.find_element_by_xpath("//input[@formcontrolname='account']").send_keys(u'43072320801') #输入账号
time.sleep(2)

driver.find_element_by_xpath(my.xpath1).send_keys(my.account) #输入账号
#time.sleep(1)

driver.find_element_by_xpath(my.xpath2).send_keys(my.password) #输入密码
yanzhengma = input("请手动输入验证码：")
driver.find_element_by_xpath(my.xpath3).send_keys(yanzhengma) #输入验证码
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
time.sleep(5)

#显示查询画面
#driver.find_element_by_xpath("//input[@formcontrolname='aab002']").send_keys(u'张梅') #输入查询人姓名
#time.sleep(2)
#！！出现重名，所以弃用

#p1 = personData.personData("李明伏","432424196404165015","13875184544","6217995580015235015","王大厦","13974204998","96")
#p1 = personData.personData("李明伏","432424196404165015","13875184544","6217995580015235015","王自平","13974204998","96")
#e_to_j.save_as_json(list_poor_family,'002.json')

try:
    #for p1 in list(reversed(list_poor_family[:])):
    for p1 in list_poor_family:
        try:
            #if p1.suoyin.endswith("50"):
            
            #if error_count>=300:  #错误计数开关
            #    break
            if (p1.edit == False and p1.error == False):
                e_to_j.personDatalist_to_json(list_poor_family,'002.json')
                time.sleep(1)
                try:
                    driver.find_element_by_xpath(my.xpath9).clear() #清空
                    driver.find_element_by_xpath(my.xpath9).send_keys(p1.ID) #输入查询人身份证号
                    time.sleep(1)
                    driver.find_element_by_xpath(my.xpath10).click() #点击查询按钮
                    time.sleep(1)
                    #！！如果查询不到  异常处理   记录日志    保存日志
                    #driver.find_element_by_xpath("//*[@id="ui-tabpanel-1"]/div/busi-tab/object-poor-family/p-panel[3]/div/div[2]/div/div/object-poor-family-grid/p-datatable/div/div[1]/div/div[2]/div/table/tbody/tr/td[4]/span/span").click() #点击第一栏查询项姓名栏（如果查询结果唯一）
                    #time.sleep(2)
                    driver.find_element_by_xpath(my.xpath11).click() #点击第一栏查询项姓名栏（如果查询结果唯一）
                    time.sleep(1)


                    #driver.find_element_by_xpath(my.xpath12).clear()
                    #driver.find_element_by_xpath(my.xpath12).send_keys(p1.phone)
                    #time.sleep(0.5)
                    ##formcontrolname="aar012" 联系电话
                    #driver.find_element_by_xpath(my.xpath13).clear()
                    #driver.find_element_by_xpath(my.xpath13).send_keys(p1.cardnumber)#录入银行卡号
                    #time.sleep(1)
                    ##formcontrolname="aac004" 银行卡号
                    #driver.find_element_by_xpath(my.xpath27).click()#点击页面保存
                    #time.sleep(1)
                    #driver.find_element_by_xpath(my.xpath26).click()#点击确定
                    #time.sleep(0.5)


                except (ElementNotVisibleException,NoSuchElementException,TimeoutException)as e:    
                    print("009")
                    p1.add_log_e1(e)
                    p1.show_error()     
                    error_count+=1
                    continue
                
                #基础信息修改完毕
                
                #开始修改结对帮扶人信息
                driver.find_element_by_xpath(my.xpath14).click() #点击帮扶责任人结对信息栏
                time.sleep(2)
                
                try:#判定是否发现该结对帮扶人
                    driver.find_element_by_xpath("//span[contains(text(),'%s')]"% p1.helpPerson)
                    a=True
                except NoSuchElementException:
                    a=False
                if a:                    
                    #通过姓名定位后获取编号和电话号码
                    if driver.find_element_by_xpath("//span[contains(text(),'%s')]/../../td[14]/span"% p1.helpPerson).text == p1.helpPerson_phone and driver.find_element_by_xpath("//span[contains(text(),'%s')]/../../td[6]/span/span"% p1.helpPerson).text != p1.startdate:#如果联系电话一致，且开始日期不为"2018年06年01日"，则需要先判定序号，为1时直接执行修改日期程序，不为1时，先js注入，点击radio，再执行修改程序。保存后。保存edit log

                        #判定序号
                        if driver.find_element_by_xpath("//span[contains(text(),'%s')]/../../td[14]/span" % p1.helpPerson).text != "1" :
                            #注入js 模拟点击radio
                            #js = "$('object-poor-family-twinning-grid>p-datatable>div>div>div>:nth-child(2)>div>table>:nth-child(2)>:nth-child(%d)>td>p-dtradiobutton>div>div:nth-child(2)>span').click()" % int(driver.find_element_by_xpath("//span[contains(text(),'%s')]/../../td[14]/span" % p1.helpPerson).text)
                            #driver.execute_script(js)

                            #也可以直接点击input下的span
                            driver.find_element_by_xpath("//span[contains(text(),'%s')]/../../td[1]/*/*/div[2]/span"% p1.helpPerson).click()

                        driver.find_element_by_xpath(my.xpath17).click()#点击修改日期按钮
                        time.sleep(1)
                        driver.find_element_by_xpath(my.xpath18).clear()#清除开始日期
                        driver.find_element_by_xpath(my.xpath18).send_keys(p1.startdate)#输入开始日期
                        driver.find_element_by_xpath(my.xpath19).clear()#清除结束日期
                        driver.find_element_by_xpath(my.xpath19).send_keys(p1.enddate)#输入结束日期
                        driver.find_element_by_xpath(my.xpath20).click()#点击保存按钮
                        time.sleep(1)
                        try:
                            driver.find_element_by_xpath(my.xpath26).click()#点击上层确定按钮
                        except :
                            print("001")
                            driver.find_element_by_xpath(my.xpath36).click()#点击 添加修改帮扶日期页面关闭X按钮
                            time.sleep(0.5)
                            driver.find_element_by_xpath(my.xpath28).click()#点击贫困户信息页关闭按钮
                            time.sleep(0.5)
                            driver.find_element_by_xpath(my.xpath26).click()#点击上层确定按钮
                            p1.show_editdate()
                            continue

                        time.sleep(0.5)
                        driver.find_element_by_xpath(my.xpath28).click()#点击贫困户信息页关闭按钮
                            
                        p1.show_editdate()
                        continue
                    else: #无需修改
                        if p1.error== True:
                            print("该户上次录入时出错，跳过，待手工处理（）")
                        driver.find_element_by_xpath(my.xpath28).click()#点击贫困户信息页关闭按钮
                        p1.pass_state()
                        continue

                    #移除按钮的隐藏类名，使其可见
                    #js = "document.querySelector('object-poor-family-twinning-grid>p-datatable>div>div>div>:nth-child(2)>div>table>:nth-child(2)>:nth-child(%d)>td>p-dtradiobutton>div>div:nth-child(1)').removeClass"% n   N表示第几行
                    #driver.execute_script(js)

                    #:nth-child(n) 第N个子元素

                    # object-poor-family-twinning-grid>p-datatable>div>div>div>:nth-child(2)>div>table>:nth-child(2)>:nth-child(1)>td>p-dtradiobutton>div>div   已结对帮扶责任人列表第一个radioselector 用于移除class
                    # object-poor-family-twinning-grid>p-datatable>div>div>div>:nth-child(2)>div>table>:nth-child(2)>:nth-child(2)>td>p-dtradiobutton>div>div   已结对帮扶责任人列表第一个radioselector 用于移除class
                    # object-poor-family-twinning-grid>p-datatable>div>div>div>:nth-child(2)>div>table>:nth-child(2)>:nth-child(3)>td>p-dtradiobutton>div>div   已结对帮扶责任人列表第一个radioselector 用于移除class

                    # //object-poor-family-twinning-grid/p-datatable/div/div[1]/div/div[2]/div/table/tbody/tr[%d]/td[2]/span/span % n 第n栏编号元素的xpath(编号1,2,3)
                    # //object-poor-family-twinning-grid/p-datatable/div/div[1]/div/div[2]/div/table/tbody/tr[%d]/td[3]/span % n 第n栏 姓名 元素的xpath
                    # //object-poor-family-twinning-grid/p-datatable/div/div[1]/div/div[2]/div/table/tbody/tr[%d]/td[4]/span % n 第n栏 单位 元素的xpath
                    # //object-poor-family-twinning-grid/p-datatable/div/div[1]/div/div[2]/div/table/tbody/tr[%d]/td[6]/span/span % n 第n栏 开始日期 元素的xpath
                    # //object-poor-family-twinning-grid/p-datatable/div/div[1]/div/div[2]/div/table/tbody/tr[%d]/td[7]/span/span % n 第n栏 结束日期 元素的xpath
                    # //object-poor-family-twinning-grid/p-datatable/div/div[1]/div/div[2]/div/table/tbody/tr[%d]/td[14]/span % n 第n栏 联系电话 元素的xpath
                    # driver.find_elements_by_xpath("").text 获取元素的文本值
                    # //span[contains(text(),'%s')]/../../td[2]/span/span  根据姓名查找序号
                    # //span[contains(text(),'%s')]/../../td[14]/span  根据姓名查找联系电话
                    # //span[contains(text(),'%s')]/../../td[6]/span/span  根据姓名查找开始结对日期
                    # //span[contains(text(),'孙军')]/../../td[1]/*/*/*/*  根据姓名查找radio/input
                    #相邻元素定位，
                    #前一位：
                    #preceding-sibling::div[1]
                    #后一位：
                    #following-sibling::div[1]
                    #前N位：
                    #preceding-sibling::div[N]
                    #后N位：
                    #following-sibling::div[N]

                    #思路1：破解display:none问题  先通过xpath文本查找（帮扶人姓名、电话、开始、结束他日期）确定需要修改的行号，然后根据行号使用js（CSSselector）注入移除类名，实现点击radio

                    #思路2：通过xpath文本查找（帮扶人姓名、电话、开始、结束他日期）判定是否需要修改，同时确定行号后，删除多余行，使待编辑行变为首行

                else:#否则点击新增结对帮扶人
                    try:
                        driver.find_element_by_xpath(my.xpath16).click()#新增结对
                        time.sleep(0.5)
                        driver.find_element_by_xpath(my.xpath21).send_keys(p1.helpPerson)#输入结对帮扶人姓名
                        driver.find_element_by_xpath(my.xpath22).click()#点击查询
                        time.sleep(0.5)
                        driver.find_element_by_xpath(my.xpath24).send_keys(p1.startdate)
                        driver.find_element_by_xpath(my.xpath25).send_keys(p1.enddate)
                        try:
                            driver.find_element_by_xpath(my.xpath23).click()#点击保存
                            time.sleep(1)
                            
                            driver.find_element_by_xpath(my.xpath26).click()#点击上层确定
                            time.sleep(0.5)
                            p1.add_log_finish()
                            p1.show_edit()
                            
                        except (ElementNotVisibleException,NoSuchElementException,TimeoutException)as e:
                            print("003")
                            p1.add_log_e0(e)
                            p1.show_error()
                            try:
                                driver.find_element_by_xpath(my.xpath34).click()#添加结对帮扶责任人列表关闭X按钮
                            except :
                                print("........")
                                pass

                            time.sleep(1)
                            driver.find_element_by_xpath(my.xpath28).click()#点击贫困户信息页关闭按钮
                            time.sleep(0.5)
                            continue


                        
                
                    except(ElementNotVisibleException,NoSuchElementException,TimeoutException)as e:
                        print("004")
                        p1.add_log_e2(e)
                        p1.show_error()                        
                        #continue
                
                try:
                    #driver.find_element_by_xpath(my.xpath27).click()#点击页面保存
                    #time.sleep(1)
                    #try:
                    #    driver.find_element_by_xpath(my.xpath26).click()#点击确定
                    #except :
                    #    pass
                    time.sleep(0.5)
                    driver.find_element_by_xpath(my.xpath28).click()#关闭弹出页面
                    time.sleep(0.5)
                    
                except(ElementNotVisibleException,NoSuchElementException,TimeoutException)as e:
                    print("005")
                    p1.add_log_e(e)
                    p1.show_error()
                    #continue
            else:
                p1.pass_state()
                
        except (ElementNotVisibleException,NoSuchElementException,TimeoutException)as e:
            
            print(e)
            input()
            error_count+=1
            try:
                driver.find_element_by_xpath(my.xpath26).click()#整体确定关闭X按钮
            except :
                print("debug4")
            try:
                driver.find_element_by_xpath(my.xpath34).click()#添加结对帮扶责任人列表关闭X按钮
            except :
                print("debug1")
            try:
                driver.find_element_by_xpath(my.xpath26).click()#整体确定关闭X按钮
            except :
                print("debug4")
            try:
                driver.find_element_by_xpath(my.xpath35).click()#贫困户信息关闭X按钮
            except :
                print("debug2")
            try:
                driver.find_element_by_xpath(my.xpath26).click()#整体确定关闭X按钮
            except :
                print("debug4")
    
            continue
except (ElementNotVisibleException,NoSuchElementException,TimeoutException)as e:
    print(e)
    print("007")
    error_count+=1
    pass
finally:
    print ("0000000")
    e_to_j.personDatalist_to_json(list_poor_family,'002.json')







    






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








