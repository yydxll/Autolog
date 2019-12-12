import xlwt
import calendar


def person():
    monthRange = calendar.monthrange(2019, 8)
    daycount = monthRange[1]
    print(daycount)

    workbook = xlwt.Workbook(encoding='utf-8')  # 新建工作簿
    sheet1 = workbook.add_sheet("汇总")  # 新建汇总
    if (daycount == 31):
        sheet2 = workbook.add_sheet("1")
        sheet3 = workbook.add_sheet("2")
        sheet4 = workbook.add_sheet("3")
        sheet5 = workbook.add_sheet("4")
        sheet6 = workbook.add_sheet("5")
        sheet7 = workbook.add_sheet("6")
        sheet8 = workbook.add_sheet("7")
        sheet9 = workbook.add_sheet("8")
        sheet10 = workbook.add_sheet("9")
        sheet11 = workbook.add_sheet("10")
        sheet12 = workbook.add_sheet("11")
        sheet13 = workbook.add_sheet("12")
        sheet14 = workbook.add_sheet("13")
        sheet15 = workbook.add_sheet("14")
        sheet16 = workbook.add_sheet("15")
        sheet17 = workbook.add_sheet("16")
        sheet18 = workbook.add_sheet("17")
        sheet19 = workbook.add_sheet("18")
        sheet20 = workbook.add_sheet("19")
        sheet21 = workbook.add_sheet("20")
        sheet22 = workbook.add_sheet("21")
        sheet23 = workbook.add_sheet("22")
        sheet24 = workbook.add_sheet("23")
        sheet25 = workbook.add_sheet("24")
        sheet26 = workbook.add_sheet("25")
        sheet27 = workbook.add_sheet("26")
        sheet28 = workbook.add_sheet("27")
        sheet29 = workbook.add_sheet("28")
        sheet30 = workbook.add_sheet("29")
        sheet31 = workbook.add_sheet("30")
        sheet32 = workbook.add_sheet("31")
    else:
        sheet2 = workbook.add_sheet("1")
        sheet3 = workbook.add_sheet("2")
        sheet4 = workbook.add_sheet("3")
        sheet5 = workbook.add_sheet("4")
        sheet6 = workbook.add_sheet("5")
        sheet7 = workbook.add_sheet("6")
        sheet8 = workbook.add_sheet("7")
        sheet9 = workbook.add_sheet("8")
        sheet10 = workbook.add_sheet("9")
        sheet11 = workbook.add_sheet("10")
        sheet12 = workbook.add_sheet("11")
        sheet13 = workbook.add_sheet("12")
        sheet14 = workbook.add_sheet("13")
        sheet15 = workbook.add_sheet("14")
        sheet16 = workbook.add_sheet("15")
        sheet17 = workbook.add_sheet("16")
        sheet18 = workbook.add_sheet("17")
        sheet19 = workbook.add_sheet("18")
        sheet20 = workbook.add_sheet("19")
        sheet21 = workbook.add_sheet("20")
        sheet22 = workbook.add_sheet("21")
        sheet23 = workbook.add_sheet("22")
        sheet24 = workbook.add_sheet("23")
        sheet25 = workbook.add_sheet("24")
        sheet26 = workbook.add_sheet("25")
        sheet27 = workbook.add_sheet("26")
        sheet28 = workbook.add_sheet("27")
        sheet29 = workbook.add_sheet("28")
        sheet30 = workbook.add_sheet("29")
        sheet31 = workbook.add_sheet("30")

    workbook.save(r'E:\NXY2\galaxy-mivs\trunk\01_项目管理\01项目日报\2019年\7月\日报-201912-李爽.xls')  # 保存
    # sheet=[sheet2]
    # for sh in sheet:
    #     print(sh)
    #     sh.write_merge(0, 0, 0, 7, '工作日报')  # 合并行单元格
    #     print("cha")
    # # os.makedirs(r'E:\NXY2\galaxy-mivs\trunk\01_项目管理\01项目日报\2019年\7月')
    # print("创建个人表格成功")
    sheet2.col(0).width = 2500
    sheet2.col(1).width = 2500
    sheet2.col(2).width = 4500
    sheet2.col(3).width = 4500
    sheet2.col(4).width = 4500
    sheet2.col(5).width = 4000

    # sheet2.row(0).height = 5000
    # sheet2.row(1).height = 5000
    # sheet2.row(2).height = 5000
    # sheet2.row(3).height = 5000
    # sheet2.row(4).height = 5000
    # sheet2.row(5).height = 5000
    # sheet2.row(6).height = 5000
    # sheet2.row(7).height = 5000
    # property = {
    #     'font_size': 11,  # 字体大小
    #     'bold': True,  # 是否加粗
    #     'align': 'left',  # 水平对齐方式
    #     'valign': 'vcenter',  # 垂直对齐方式
    #     'font_name': u'微软雅黑',
    #     'text_wrap': False,  # 是否自动换行
    # }
    # cell_format = workbook.add_format(property)
    sheet2.write(1,3,'项目名称：辽宁农信\r\n统一支付平台改造项\r\n目')
    sheet2.write(1,4,'工作量合计（小时）：')


    # sheet2.write('项目名称：辽宁农信统一支付平台改造项目', font=("Arial", 18, "normal"))


    sheet2.write_merge(0, 0, 0, 5, '工作日报')
    sheet2.write_merge(1, 1, 0, 2, '公司名称：神州数码融信科技有限公司')
    # sheet2.write_formula()#公式
    style = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')#设置成黄色
    sheet2.write(2, 5, '2019/12/1', style)

    sheet2.row(0).set_style(xlwt.easyxf('font:height 720;'))#第一行行高
    sheet2.row(1).set_style(xlwt.easyxf('font:height 720;'))
    sheet2.row(2).set_style(xlwt.easyxf('font:height 680;'))
    sheet2.row(3).set_style(xlwt.easyxf('font:height 680;'))
    for i in range(2,16):
        sheet2.row(i).set_style(xlwt.easyxf('font:height 500;'))


    # sheet2.row(4).set_style(xlwt.easyxf('font:height 500;'))
    # sheet2.row(5).set_style(xlwt.easyxf('font:height 500;'))
    # sheet2.row(6).set_style(xlwt.easyxf('font:height 500;'))
    # sheet2.row(7).set_style(xlwt.easyxf('font:height 500;'))
    # sheet2.row(8).set_style(xlwt.easyxf('font:height 500;'))
    # sheet2.row(9).set_style(xlwt.easyxf('font:height 500;'))
    # sheet2.row(10).set_style(xlwt.easyxf('font:height 500;'))
    # sheet2.row(11).set_style(xlwt.easyxf('font:height 500;'))
    # sheet2.row(12).set_style(xlwt.easyxf('font:height 500;'))
    # sheet2.row(13).set_style(xlwt.easyxf('font:height 500;'))
    # sheet2.row(14).set_style(xlwt.easyxf('font:height 500;'))
    # sheet2.row(15).set_style(xlwt.easyxf('font:height 500;'))




    #
    # tall_style = xlwt.easyxf('font:height 720;')  # 36pt,类型小初的字号
    # first_row = sheet2.row(0)
    # first_row.set_style(tall_style)

    workbook.save(r'E:\NXY2\galaxy-mivs\trunk\01_项目管理\01项目日报\2019年\7月\日报-201912-李爽.xls')  # 保存


person()
