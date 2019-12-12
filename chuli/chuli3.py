import xlrd
import xlwt
from xlutils.copy import copy


def gaiming(wenjian, name,logyear,logmonth):
    name = "姓名：" + name
    tem_excel = xlrd.open_workbook(wenjian, formatting_info=True)
    wb = copy(tem_excel)
    style = xlwt.XFStyle()  # 格式信息
    font = xlwt.Font()  # 字体基本设置
    font.height = 220
    font.name = u'宋体'
    font.bold = True
    style.font = font

    alignment = xlwt.Alignment()  # 设置字体在单元格的位置
    # alignment.horz = xlwt.Alignment.HORZ_CENTER #水平方向
    alignment.vert = xlwt.Alignment.VERT_CENTER  # 竖直方向
    style.alignment = alignment
    for i in range(1,31):
        s = wb.get_sheet(i)

        s.write(2, 1, name, style)

        # s.write_formula(1, 6, '=F7 + B4')
        s.write(2,6,str(logyear)+'/'+str(logmonth)+'/'+str(i),style)
    wb.save(wenjian)  # 保存