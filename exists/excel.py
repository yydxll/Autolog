import os
from exists import person

def excel():
    if not os.path.exists(r'E:\NXY2\galaxy-mivs\trunk\01_项目管理\01项目日报\2019年\7月\日报-201912-李爽.xls'):
        person()
        print("创建个人表格成功")


excel()
