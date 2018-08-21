class personData():
    """储存待录入结对帮扶资料对象"""
    def __init__(self,name,ID,phone,cardnumber,helpPerson,startdate='2018年6月1日',enddate='2020年12月31日'):
        self.name = name
        self.ID = ID
        self.phone = phone
        self.cardnumber = cardnumber
        self.helpPerson = helpPerson
        self.startdate = startdate
        self.enddate = enddate



