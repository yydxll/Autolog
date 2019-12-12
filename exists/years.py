import os
def year(address):
    if not os.path.exists(address):
        os.makedirs(address)
        print("创建年份文件夹成功")
    else:
        print("年份文件夹已存在")
