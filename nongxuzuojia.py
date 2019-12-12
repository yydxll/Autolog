import configparser
import random
import re
import calendar
from chuli import chuli
def zhinengchuli():
    conf = configparser.ConfigParser()
    conf.read(r'xml\config.ini', encoding='UTF-8')
    path = conf.get('xml01', 'txtpath')  # 导入config配置文件中的日志txt文件目录
    with open(path, "r", encoding='utf-8') as f:
        data = f.read()
    Author = re.findall('/*?\|(.*?)\|.*?\|.*?\|.*?\|', data)  # dzq
    Message = re.findall('20.*?\|.*?\|(.*?)\|', data)  # 修改
    Date = re.findall('(\d\d\d\d\d\d\d\d)\|', data) # 20190904
    DateMonth=re.findall('\d\d\d\d(\d\d)\d\d\|', data)
    Webaddress = re.findall('20.*?\|.*?\|.*?\|.*?\|(.*?)\|', data)  # cnaps|
    hour = re.findall('20.*?\|.*?\|.*?\|(.*?)\|.*?\|', data)  # 4
    year=re.findall('(\d\d\d\d)\d\d\d\d\|', data)
    DateDay=re.findall('\d\d\d\d\d\d(\d\d)\|', data)
    # sortDate=int(Date).sort()
    # print(sortDate)
    stringlist=[]
    for i in range (len(Author)):
        string=Date[i]+'|'+Author[i]
        stringlist.append(string)
    conf = configparser.ConfigParser()
    conf.read(r'xml\config.ini', encoding='UTF-8')
    afamilynumber001 = conf.get('namelist', 'afamilynumber001')
    afamilynumber002 = conf.get('namelist', 'afamilynumber002')
    afamilynumber003 = conf.get('namelist', 'afamilynumber003')
    afamilynumber004 = conf.get('namelist', 'afamilynumber004')
    afamilynumber005 = conf.get('namelist', 'afamilynumber005')
    afamilynumber006 = conf.get('namelist', 'afamilynumber006')
    afamilynumber007 = conf.get('namelist', 'afamilynumber007')
    afamilynumber008 = conf.get('namelist', 'afamilynumber008')
    afamilynumber009 = conf.get('namelist', 'afamilynumber009')
    afamilynumber010 = conf.get('namelist', 'afamilynumber010')
    afamilynumber011 = conf.get('namelist', 'afamilynumber011')
    afamilynumber012 = conf.get('namelist', 'afamilynumber012')
    afamilynumber013 = conf.get('namelist', 'afamilynumber013')
    afamilynumber014 = conf.get('namelist', 'afamilynumber014')
    afamilynumber015 = conf.get('namelist', 'afamilynumber015')
    afamilynumber016 = conf.get('namelist', 'afamilynumber016')
    afamilynumber017 = conf.get('namelist', 'afamilynumber017')
    afamilynumber018 = conf.get('namelist', 'afamilynumber018')
    afamilynumber019 = conf.get('namelist', 'afamilynumber019')
    information1 = conf.get('information', 'information1')
    information2 = conf.get('information', 'information2')
    information3 = conf.get('information', 'information3')
    information4 = conf.get('information', 'information4')
    information5 = conf.get('information', 'information5')
    information6 = conf.get('information', 'information6')
    information7 = conf.get('information', 'information7')
    information8 = conf.get('information', 'information8')
    information9 = conf.get('information', 'information9')
    information10 = conf.get('information', 'information10')





    monthRange = calendar.monthrange(int(year[0]),int(DateMonth[0]))
    namelist=[afamilynumber001,afamilynumber002,afamilynumber003,afamilynumber004,afamilynumber005,afamilynumber006,afamilynumber007,afamilynumber008,afamilynumber009,afamilynumber010,afamilynumber011,afamilynumber012,afamilynumber013,afamilynumber014,afamilynumber015,afamilynumber016,afamilynumber017,afamilynumber018,afamilynumber019]
    information=[information1,information2,information3,information4,information5,information6,information7,information8,information9,information10]
    time=['1','2','3']
    system=['cnaps','ibps','mivs','netpay','nps']
    file = open(path, 'a', encoding='utf-8')
    # print(information1)

    file.write('\n')
    for i in range(monthRange[1]):#n月有多少天
        if(i>=int(DateDay[0])):#日志上第一天（也许是23，就是23，24，25。。。）之后开始
            first=year[0]+DateMonth[0]+str(i)#拼接字符串（20191023，20191024）
            for j in namelist:
                second=first+'|'+j
                # print(second)
                if(second not in stringlist):
                    randominformation= random.choice(information)

                    randomtime=random.choice(time)
                    randomsystem=random.choice(system)
                    result=second+'|'+randominformation+'|'+randomtime+'|'+randomsystem+'|'
                    file = open(path, 'a', encoding='utf-8')

                    file.write(result+'\n')
    file.close()
    print('文件写入')
    chuli.chuli()
# zhinengchuli()