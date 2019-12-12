import xlrd
import xlwt
from xlutils.copy import copy


def chuli5(wenjian,mm):
    tem_excel = xlrd.open_workbook(wenjian, formatting_info=True)
    wb = copy(tem_excel)

    style = xlwt.XFStyle()  # 格式信息
    font = xlwt.Font()  # 字体基本设置
    font.height = 220
    font.name = u'宋体'
    font.bold = True
    style.font = font
    alignment = xlwt.Alignment()  # 设置字体在单元格的位置
    alignment.vert = xlwt.Alignment.VERT_CENTER  # 竖直方向
    style.alignment = alignment

    for i in range(1,30):
        s = wb.get_sheet(i)
        # print(mm[i])
        s.write(1, 6,mm[i-1], style)
    wb.save(wenjian)  # 保存