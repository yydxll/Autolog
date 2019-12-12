import xlrd
import xlwt
from xlutils.copy import copy

# wenjian = r"E:\NXY2\galaxy-mivs\trunk\01_项目管理\01项目日报\2019年\7月\日报-201912-李爽.xls"
# month = 7
# name = "王洪宝"
# datapage = 1
# message1 = "增加机构代码和全辖标志"


# data="2019/12/1"

class wanghongbao:
    def huizong(self, month, name, wenjian):
        tem_excel = xlrd.open_workbook(wenjian, formatting_info=True)
        wb = copy(tem_excel)
        s = wb.get_sheet(0)

        message = (str(month) + "月份" + name + "工作日报")
        print(message)

        style = xlwt.XFStyle()  # 格式信息
        font = xlwt.Font()  # 字体基本设置
        font.height = 360
        font.name = u'宋体'
        font.bold = True
        style.font = font

        alignment = xlwt.Alignment()  # 设置字体在单元格的位置
        alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平方向
        alignment.vert = xlwt.Alignment.VERT_CENTER  # 竖直方向
        style.alignment = alignment

        s.write(0, 0, message, style)
        wb.save(wenjian)  # 保存

    def day(self, name, Today, logday, wenjian):
        tem_excel = xlrd.open_workbook(wenjian, formatting_info=True)
        wb = copy(tem_excel)
        name = "姓名：" + name
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

        s = wb.get_sheet(logday)
        s.write(2, 1, name, style)
        s.write(2, 6, Today, style)
            # print('')
        wb.save(wenjian)  # 保存
    # def hour(self, hour, data, wenjian):
    #     tem_excel = xlrd.open_workbook(wenjian, formatting_info=True)
    #     wb = copy(tem_excel)
    #     s = wb.get_sheet(data)
    #
    #     # message = (str(month) + "月份" + name + "工作日报")
    #     # print(message)
    #
    #     style = xlwt.XFStyle()  # 格式信息
    #     font = xlwt.Font()  # 字体基本设置
    #     font.height = 220
    #     font.name = u'宋体'
    #     # font.bold = True#加粗
    #     style.font = font
    #
    #     alignment = xlwt.Alignment()  # 设置字体在单元格的位置
    #     alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平方向
    #     alignment.vert = xlwt.Alignment.VERT_CENTER  # 竖直方向
    #     style.alignment = alignment
    #
    #     s.write(1, 6, hour, style)
    #     wb.save(wenjian)  # 保存


    def daybyday(self, message1, data, wenjian,hour):#写入信息和时间
        tem_excel = xlrd.open_workbook(wenjian, formatting_info=True)
        wb = copy(tem_excel)
        s = wb.get_sheet(data)

        # message = (str(month) + "月份" + name + "工作日报")
        # print(message)

        style = xlwt.XFStyle()  # 格式信息
        font = xlwt.Font()  # 字体基本设置
        font.height = 220
        font.name = u'宋体'
        # font.bold = True#加粗
        style.font = font

        alignment = xlwt.Alignment()  # 设置字体在单元格的位置
        alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平方向
        alignment.vert = xlwt.Alignment.VERT_CENTER  # 竖直方向
        style.alignment = alignment

        s.write(6, 3, message1, style)
        s.write(6, 5, hour, style)
        wb.save(wenjian)  # 保存
    def daybyday2(self, message1, data, wenjian,hour):
        tem_excel = xlrd.open_workbook(wenjian, formatting_info=True)
        wb = copy(tem_excel)
        s = wb.get_sheet(data)

        # message = (str(month) + "月份" + name + "工作日报")
        # print(message)

        style = xlwt.XFStyle()  # 格式信息
        font = xlwt.Font()  # 字体基本设置
        font.height = 220
        font.name = u'宋体'
        # font.bold = True#加粗
        style.font = font

        alignment = xlwt.Alignment()  # 设置字体在单元格的位置
        alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平方向
        alignment.vert = xlwt.Alignment.VERT_CENTER  # 竖直方向
        style.alignment = alignment

        s.write(7, 3, message1, style)
        s.write(7, 5, hour, style)
        wb.save(wenjian)  # 保存
