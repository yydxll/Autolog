from zhengze import dazhengze
import configparser


def chuli(logyear, logmonth, llogmonth, llogday,name):
    conf = configparser.ConfigParser()
    conf.read(r'xml\config.ini', encoding='UTF-8')#好的

    addressyear = conf.get('xml01', 'addressyear')  # E:\NXY2\galaxy-mivs\trunk\01_项目管理\01项目日报
    addressyear = '{}\{}年'.format(addressyear, logyear)  # E:\NXY2\galaxy-mivs\trunk\01_项目管理\01项目日报\2019年
    addressmonth = '{}\{}月'.format(addressyear, logmonth)  # E:\NXY2\galaxy-mivs\trunk\01_项目管理\01项目日报\2019年\8月

    mubanpath = conf.get('xml01', 'muban')
    xls = dazhengze.dazhengze(mubanpath)
    copymubanpath = '{}\{}'.format(addressmonth, xls)  # E:\NXY2\galaxy-mivs\trunk\01_项目管理\01项目日报\2019年\8月\01.xls
    realmubanpath = '{}\{}'.format(addressmonth, '日报-' + str(logyear) + llogmonth + '-' + name + '.xls')
    # realmubanpath = '{}\{}'.format(addressmonth, '日报-' + str(logyear) + llogmonth + '-' + name + '.xlsx')

    # E:\NXY2\galaxy-mivs\trunk\01_项目管理\01项目日报\2019年\8月\日报-201908-李爽.xls
    Today = '{}/{}/{}'.format(str(logyear), llogmonth, llogday)
    # print(copymubanpath)
    print(realmubanpath)
    print(Today)#
    return addressyear, addressmonth, realmubanpath, mubanpath, copymubanpath,Today