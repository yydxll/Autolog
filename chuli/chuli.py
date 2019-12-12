# logmonth = 8
# llogmonth = "08"
# logyear = 2019
# name = "王洪宝"
# logday = 1
# llogday = '01'
# message1 = "增加机构代码和全辖标志"
import configparser
import re

import xlrd
import xlwt
from xlutils.copy import copy

import runrunrun
from chuli import chuli2
from zhengze import opentxt
from chuli import chuli3
from chuli import chuli4
from chuli import chuli5

def chuli():
    alllist = opentxt.txtzhengze()
    conf = configparser.ConfigParser()
    conf.read(r'xml\config.ini', encoding='UTF-8')

    for i in range(len(alllist)):
        name = alllist[i]['Author']
        bfamilynumber = conf.get('namelist', name)
        # print(bfamilynumber)
        # if (alllist[i]['Author'] == name):
        alllist[i]['Author'] = bfamilynumber

        message1 = alllist[i]['Message']
        name = alllist[i]['Author']
        logyear = alllist[i]['Date'][0:4]
        llogmonth = re.findall('\d\d\d\d(\d\d)\d\d', alllist[i]['Date'])[0]

        llogday = re.findall('\d\d\d\d\d\d(\d\d)', alllist[i]['Date'])[0]
        Web=(alllist[i]['webaddress'])
        # print(logmonth)
        hour=alllist[i]['hour'][0]
        # print(Web)
        if (llogmonth.startswith('0')):
            logmonth=llogmonth[1:]
        else:
            logmonth = llogmonth
        if (llogday).startswith('0'):
            logday = llogday[1:]
        else:
            logday = str(llogday)
        if(alllist[i]['Author']==alllist[i-1]['Author'] and alllist[i]['Date']==alllist[i-1]['Date']and alllist[i]['webaddress']==alllist[i-1]['webaddress']):
            samenumber=2
        else:
            samenumber=1

        addressyear, addressmonth, realmubanpath, mubanpath, copymubanpath, Today = chuli2.chuli(logyear, logmonth,
                                                                                                 llogmonth, llogday,
                                                                                                 name)
        # print('oooooooooooooooooooo:'+realmubanpath)


        runrunrun.runrunrun(addressyear, addressmonth, realmubanpath, mubanpath, copymubanpath, Today, logmonth, name,
                            logday, message1 ,hour,Web,samenumber)
        chuli3.gaiming(realmubanpath, name, logyear, logmonth)
        mm=chuli4.allconut(realmubanpath)
        chuli5.chuli5(realmubanpath,mm)


