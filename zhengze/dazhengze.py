#!/usr/bin/python
import re
def dazhengze(mubanpath):


    matchObj = re.match(r'(.*)\\(.*)',mubanpath, re.M | re.I)

    if matchObj:

        print("文件名：", matchObj.group(2))
        return matchObj.group(2)

    else:
        print("正则路径信息错误，联系作者18740058827")
