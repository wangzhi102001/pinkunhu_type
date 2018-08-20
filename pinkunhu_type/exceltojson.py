
import xlrd
from collections import OrderedDict
import json
import codecs

 

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





