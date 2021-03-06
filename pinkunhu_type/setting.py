# -*- coding:utf-8 -*-
import json
import codecs
class setting():
    """w"""
    def __init__(self,account,password):
        self.url = "http://cpadisc4.cpad.gov.cn/cpad/login"
        self.account = account
        self.password = password
        self.chromePath = u'C:/Program Files (x86)/Google/Chrome/Application/chromedriver'
        self.xpath1 = "//input[@formcontrolname='account']"#帐号输入框体
        self.xpath2 = "//input[@formcontrolname='password']"#密码输入框体
        self.xpath3 = "//input[@formcontrolname='inputCode']"#验证码输入框体
        self.xpath4 = "//span[@class='ui-button-text ui-clickable']"#首页登陆按钮
        self.xpath5 = "//a[@title='扶贫对象']"#扶贫对象菜单按钮
        self.xpath6 = "//a[@title='基础信息维护']"#扶贫对象=>基础信息子菜单按钮
        self.xpath7 = "//a[@title='2018年度']"#扶贫对象=>基础信息=>2018年度子菜单按钮
        self.xpath8 = "/html/body/app-root/div/div/app-main-layout/div/div[1]/div/div/app-menu/ul/nui-main-menu/div/div[1]/div[2]/div/nui-main-menu-sub/ul/li/nui-main-menu-sub/ul/li[6]/nui-main-menu-sub/ul/li[1]/a/span[2]"#扶贫对象=>基础信息=>2018年度=>贫困户按钮
        self.xpath9 = "//input[@formcontrolname='aab004']"#基础信息维护界面=>身份证号查询输入框体
        self.xpath10 = "//button[@label='查询']/span"#基础信息维护界面=>查询按钮
        self.xpath11 = "//p-datatable[@datakey]/*/*/*/div[2]/*/*/tbody/*/td[4]/*/span"#查询结果第一栏
        self.xpath12 = "//input[@formcontrolname='aar012']"#贫困户首页基础信息=>联系电话框体
        self.xpath13 = "//input[@formcontrolname='aac004']"#贫困户首页基础信息=>银行卡号框体
        self.xpath14 = "//span[contains(text(),'五、帮扶责任人结对信息')]"#结对帮扶人信息选项卡选择
        self.xpath15 = "//button[@label='取消结对']/span"#取消结对按钮
        self.xpath16 = "//button[@label='增加结对']/span"#增加结对按钮
        self.xpath17 = "//button[@label='修改时间']/span"#修改时间按钮
        self.xpath18 = "//object-poor-family/p-dialog[4]/div/div[2]/p-tabview/div/div/form/div/div/div[2]/nui-date-nav/div/p-calendar/span/input"#修改日期=>开始日期框体
        self.xpath19 = "//object-poor-family/p-dialog[4]/div/div[2]/p-tabview/div/div/form/div/div/div[4]/nui-date-nav/div/p-calendar/span/input"#修改日期=>结束日期框体
        self.xpath20 = "//button[@id = 'saveTime' and @label='保存']"#修改日期=>保存按钮
        self.xpath21 = "//input[@placeholder='请输入帮扶责任人姓名']"#新增结对帮扶人=>输入结对帮扶人姓名框体
        self.xpath22 = "//button[@id = 'queryByName' and @label='查询']"#新增结对帮扶人=>查询按钮
        self.xpath23 = "//button[@id='saveTwinning']/span"#新增结对帮扶人=>保存按钮
        self.xpath24 = "//object-poor-family-twinning-addgrid/form[2]/div/div/div[2]/nui-date-nav/div/p-calendar/span/input"#新增结对帮扶人=>开始日期框体
        self.xpath25 = "//object-poor-family-twinning-addgrid/form[2]/div/div/div[4]/nui-date-nav/div/p-calendar/span/input"#新增结对帮扶人=>结束日期框体
        self.xpath26 = "//button[@class='swal2-confirm swal2-styled']"#上层确定按钮
        self.xpath27 = "//button[@id='on_save']/span"#页面保存按钮
        self.xpath28 = "//button[@id='on_cancel']/span"#页面关闭按钮
        self.xpath29 = "//object-poor-family-twinning-addgrid/p-datatable/div/div/div/div[2]/div/table/tbody/tr/td/p-dtradiobutton/div/div/input"#新增结对帮扶人选择框1号
        self.xpath30 = "//object-poor-family-twinning-addgrid/p-datatable/div/div/div/div[2]/div/table/tbody/tr[2]/td/p-dtradiobutton/div/div/input"#新增结对帮扶人选择框2号
        self.xpath31 = "//object-poor-family-twinning-addgrid/p-datatable/div/div/div/div[2]/div/table/tbody/tr/td[3]/span"#新增结对帮扶人姓名（.text）
        self.xpath32 = "//object-poor-family-twinning-addgrid/p-datatable/div/div/div/div[2]/div/table/tbody/tr/td[14]/span"#新增结对帮扶人联系电话（.text）
        self.xpath33 = "//object-poor-family-twinning-grid/p-datatable/div/div[1]/div/div[2]/div/table/tbody/tr/td[3]/span"
        self.xpath34 = "//span[contains(text(),'添加帮扶责任人列表')]/../a"#添加结对帮扶责任人列表关闭X按钮
        self.xpath35 = "//span[contains(text(),'贫困户信息')]/../a"#贫困户信息关闭X按钮
        self.xpath36 = "//span[contains(text(),'修改帮扶时间')]/../a" #添加修改帮扶日期页面关闭X按钮
    
    def load_setting(self):
        with open('setting.json','r',encoding = 'utf-8') as f:
            list_f = json.load(f)
            self.account = list_f['account']
            self.password = list_f['password']
        print("已从'setting.json'加载帐号密码")

    def get_and_save_setting(self):
        account = input("请输入帐号")
        password = input("请输入密码")
        dict_j = {'account':account,'password':password}
        j_file = str(json.dumps(dict_j, ensure_ascii=False))
        with codecs.open('setting.json','w', encoding='utf-8', errors ='ignore') as f:
            f.write(j_file)
        print("已将账号和密码，保存至目录下的setting.json，可用记事本打开自行编辑，下次运行将自动读取已存配置")
            