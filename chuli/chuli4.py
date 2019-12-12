import xlrd

#打开文件
#获取表格数目
import xlwt
from xlutils.copy import copy
# realmubanpath=r'E:\NXY2\galaxy-mivs\trunk\01_项目管理\01项目日报\2019年\10月\日报-201910-杨宏岩.xls'

def allconut(realmubanpath):
    data = xlrd.open_workbook(realmubanpath)
    # wb = copy(data)
    #
    # style = xlwt.XFStyle()  # 格式信息
    # font = xlwt.Font()  # 字体基本设置
    # font.height = 360
    # font.name = u'宋体'
    # font.bold = True
    # style.font = font
    #
    # alignment = xlwt.Alignment()  # 设置字体在单元格的位置
    # alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平方向
    # alignment.vert = xlwt.Alignment.VERT_CENTER  # 竖直方向
    # style.alignment = alignment
    #根据sheet顺序打开sheet
    # sheet1 = data.sheets()[1]
    mm=[]
    for i in range(1,31):
        #根据sheet名称获取
        sheet2 = data.sheet_by_name(str(i))
        z1=sheet2.row_values(6)[5]
        # z1=int(z1)
        z2=sheet2.row_values(7)[5]
        # z2 = int(z2)
        z3=sheet2.row_values(8)[5]
        # z3 = int(z3)
        z4=sheet2.row_values(9)[5]
        # z4 = int(z4)
        z5=sheet2.row_values(10)[5]
        # z5=int(z5)
        z6=sheet2.row_values(11)[5]
        # z6 = int(z6)
        z7=sheet2.row_values(12)[5]
        # z7 = int(z7)
        z8=sheet2.row_values(13)[5]
        # z8 = int(z8)
        z9=sheet2.row_values(14)[5]
        # z9 = int(z9)
        z10=sheet2.row_values(15)[5]
        # z10=int(z10)
        if(z1==''):
            z1=0
        if(z2==''):
            z2=0
        if(z3==''):
            z3=0
        if(z4==''):
            z4=0
        if(z5==''):
            z5=0
        if(z6==''):
            z6=0
        if(z7==''):
            z7=0
        if(z8==''):
            z8=0
        if(z9==''):
            z9=0
        if(z10==''):
            z10=0
        z=int(z1)+int(z2)+int(z3)+int(z4)+int(z5)+int(z6)+int(z7)+int(z8)+int(z9)+int(z10)
        # z=str(z)
        # z=z1+z2
        # s = wb.get_sheet(i)
        # z=z1
        # print(z)
        # print(type(z6))
        # s = wb.get_sheet(i)
        mm.append(z)
        # s.write(1, 6, z, style)
        # wb.save(realmubanpath)  # 保存
    # print(mm)
    return mm
# allconut(realmubanpath)