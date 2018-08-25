from datetime import datetime
class personData():
    """储存待录入结对帮扶资料对象"""
    def __init__(self,name,ID,phone,cardnumber,helpPerson,helpPerson_phone,suoyin,edit = False,error = False,log=""):
        self.name = name
        self.ID = ID
        self.phone = phone
        self.cardnumber = cardnumber
        self.helpPerson = helpPerson
        self.helpPerson_phone = helpPerson_phone
        self.startdate = '2018年06月01日'
        self.enddate = '2020年12月31日'
        self.edit = edit
        self.suoyin = suoyin
        self.error = error
        self.log=log
        


    def show_error(self):
        
        self.error = True
        self.print_log()
    
    def show_edit(self):
        self.edit = True
        self.add_log_finish()
        self.print_log()

    def show_editdate(self):
        self.edit = True
        self.add_log_editdate()
        self.print_log()

    def end(self):
        self.edit = True
        
        self.print_log()

    def add_log_e(self,e):
        self.log = "错误，%s,%s,%s,%s 出错，（%s）"% (datetime.now(),self.suoyin,self.name,self.ID,e)

    def add_log_e1(self,e):
        self.log = "错误，%s,%s,%s,%s 身份证号有误，无法进入基础信息修改界面，（%s）。"% (datetime.now(),self.suoyin,self.name,self.ID,e)

    def add_log_e2(self):
        self.log = "错误，%s,%s,%s,%s在新增结对帮扶责任人时出错。"% (datetime.now(),self.suoyin,self.name,self.ID)
    
    def add_log_e0(self):
        self.log = "错误，%s,%s,%s,%s，尚未查询到该结对帮扶责任人 %s 时出错。"% (datetime.now(),self.suoyin,self.name,self.ID,self.helpPerson)

    def add_log_same(self):
        self.log = "提示，%s,%s,%s,%s在系统中出现相同的结对帮扶人%s,标记为已处理，待手动处理。"% (datetime.now(),self.suoyin,self.name,self.ID,self.helpPerson)

    def add_log_finish(self):

        self.log = "完成，%s,%s,%s,%s已将结对帮扶人 %s 录入系统。"% (datetime.now(),self.suoyin,self.name,self.ID,self.helpPerson)
    
    def add_log_editdate(self):

        self.log = "完成，%s,%s,%s,%s已将结对帮扶人 %s 时间修改完成。"% (datetime.now(),self.suoyin,self.name,self.ID,self.helpPerson)
    def add_pass_state(self):
        self.log = "提示：%s,%s,%s,%s状态为已修改，跳过..."% (datetime.now(),self.suoyin,self.name,self.ID)

    def print_log(self):
        print(self.log)

    def pass_state(self):
        self.edit = True
        self.add_pass_state()
        self.print_log()


