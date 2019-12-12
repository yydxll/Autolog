import xlrd
from xlutils.copy import copy

from exists import years
from exists import month
from exists import copyexcel
from fivesystem.galaxy_mivs import mivs
from fivesystem.galaxy_cnaps import cnaps
from fivesystem.galaxy_ibps import ibps
from fivesystem.galaxy_netpay import netpay
from fivesystem.galaxy_nps import nps
import os




def runrunrun(addressyear, addressmonth, realmubanpath, mubanpath, copymubanpath, Today, logmonth, name, logday,
              message1, hour, Web,samenumber):
    years.year(addressyear)
    month.month(addressmonth)
    if (os.path.exists(realmubanpath) == False):
        copyexcel.copy(mubanpath, addressmonth, copymubanpath, realmubanpath)
    else:
        print("xls文件已存在")
    if (Web == 'mivs'):
        mivs.wanghongbao().huizong(logmonth, name, realmubanpath)
        mivs.wanghongbao().day(name, Today, logday, realmubanpath)
        # mivs.wanghongbao().hour(hour, logday, realmubanpath)
        if (samenumber==1):
            mivs.wanghongbao().daybyday(message1, logday, realmubanpath,hour)
        else:
            mivs.wanghongbao().daybyday2(message1, logday, realmubanpath,hour)
    elif (Web == 'cnaps'):
        cnaps.wanghongbao().huizong(logmonth, name, realmubanpath)
        cnaps.wanghongbao().day(name, Today, logday, realmubanpath)
        # cnaps.wanghongbao().hour(hour, logday, realmubanpath)
        if (samenumber==1):
            cnaps.wanghongbao().daybyday(message1, logday, realmubanpath,hour)
        else:
            cnaps.wanghongbao().daybyday2(message1, logday, realmubanpath,hour)
    elif (Web == 'ibps'):
        ibps.wanghongbao().huizong(logmonth, name, realmubanpath)
        ibps.wanghongbao().day(name, Today, logday, realmubanpath)
        # ibps.wanghongbao().hour(hour, logday, realmubanpath)
        if (samenumber==1):
            ibps.wanghongbao().daybyday(message1, logday, realmubanpath,hour)
        else:
            ibps.wanghongbao().daybyday2(message1, logday, realmubanpath,hour)
    elif (Web == 'netpay'):
        netpay.wanghongbao().huizong(logmonth, name, realmubanpath)
        netpay.wanghongbao().day(name, Today, logday, realmubanpath)
        # netpay.wanghongbao().hour(hour, logday, realmubanpath)
        if (samenumber==1):
            netpay.wanghongbao().daybyday(message1, logday, realmubanpath,hour)
        else:
            netpay.wanghongbao().daybyday2(message1, logday, realmubanpath,hour)
    elif (Web == 'nps'):
        nps.wanghongbao().huizong(logmonth, name, realmubanpath)
        nps.wanghongbao().day(name, Today, logday, realmubanpath)
        # nps.wanghongbao().hour(hour, logday, realmubanpath)
        if (samenumber==1):
            nps.wanghongbao().daybyday(message1, logday, realmubanpath,hour)
        else:
            nps.wanghongbao().daybyday2(message1, logday, realmubanpath,hour)
    else:
        print("没在五大支付系统中找到")
