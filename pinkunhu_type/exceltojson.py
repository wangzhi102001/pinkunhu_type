
import xlrd
from collections import OrderedDict
import json
import codecs
import personData

 

def excel_json(path,path_two):
    ###将excel文件数据转换为json并保存到本地
    wb = xlrd.open_workbook(path) 

    convert_list = []
    sh = wb.sheet_by_index(0)
    title = sh.row_values(0)
    for rownum in range(1, sh.nrows):
        rowvalue = sh.row_values(rownum)
        single = OrderedDict()
        for colnum in range(0, len(rowvalue)):
            print(title[colnum], rowvalue[colnum])
            single[title[colnum]] = rowvalue[colnum]
        convert_list.append(single)
    j = str(json.dumps(convert_list,ensure_ascii=False))

    with codecs.open(path_two,"w",encoding='utf-8',errors='ignore') as f:
        f.write(j)
    print("excel转换json完成")

def save_as_json(object,file_path):
    with open(file_path,"w",encoding='utf-8',errors='ignore') as f:
        json.dump(object,f,ensure_ascii=False)


def file_to_json_fomat(path1,path2,personDatas,list_poor_family):
    with open(path1,'r',encoding ="utf-8")as f:#加载json文件
        personDatas =json.load(f)#将加载的json文件转换成字典列表

    for person in personDatas:
        list_poor_family.append({'name':person['name'],'ID':person['ID'],'phone':person['phone'],'cardnumber':person['cardnumber'],'helpPerson':person['helpPerson'],'helpPerson_phone':person['helpPerson_phone'],'suoyin':person['suoyin'],'edit':False,'error':False})

    save_as_json(list_poor_family,path2)



def json_to_personDatalist(path,list_js,list,error,start,end,n):
    with open('002.json','r',encoding ="utf-8")as f:#加载json文件
        list_js =json.load(f)#将加载的json文件转换成字典列表
#input()

    for person in list_js:#将加载的json数据添加到personData列表中
        list.append(personData.personData(person['name'],person['ID'],person['phone'],person['cardnumber'],person['helpPerson'],person['helpPerson_phone'],person['suoyin']))
        if not(person['edit']):
            if person['error']:
                error+=1
            start+=1
        else:
            end+=1
        n+=1
        print("已添加%s"% n)
    print("总共添加%s项,%s项已完成，%s项待完成(其中%s项出错，待手工处理)"% (n,end,start,error))
    print('''待录入数据准备完成，开始登陆系统，gogogo！！！按任意键继续，将自动开始启动Chrome浏览器
    随后请在此窗口输入验证码''')
    input()

def personDatalist_to_json(personDatalist,path):
    temp=[]

    with open('002.json','r',encoding ="utf-8")as f:#加载json文件
        list_js =json.load(f)#将加载的json文件转换成字典列表
#input()

    for person in personDatalist:
        temp.append({'name':person.name,'ID':person.ID,'phone':person.phone,'cardnumber':person.cardnumber,'helpPerson':person.helpPerson,'helpPerson_phone':person.helpPerson_phone,'suoyin':person.suoyin,'edit':person.edit,'error':person.error,'log':person.log})
    save_as_json(temp,path)
    print("已将处理后的情况保存到002.json文件中，下次运行将直接读取进度")
    




