import os
def month(addressmonth):
    if not os.path.exists(addressmonth):
        os.makedirs(addressmonth)
        print("创建月份文件夹成功")
    else:
        print("月份文件夹已存在")
