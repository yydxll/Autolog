import configparser
import re


def txtzhengze():
    conf = configparser.ConfigParser()
    conf.read(r'xml\config.ini', encoding='UTF-8')
    path = conf.get('xml01', 'txtpath')  # 导入config配置文件中的日志txt文件目录
    # path = "E:\\b.txt"
    with open(path, "r", encoding='utf-8') as f:
        data = f.read()
    Author = re.findall('/*?\|(.*?)\|.*?\|.*?\|.*?\|', data)  # dzq
    Message = re.findall('20.*?\|.*?\|(.*?)\|', data)  # 修改
    Date = re.findall('(\d\d\d\d\d\d\d\d)\|', data)  # 20190904
    Webaddress = re.findall('20.*?\|.*?\|.*?\|.*?\|(.*?)\|', data)  # cnaps|
    hour = re.findall('20.*?\|.*?\|.*?\|(.*?)\|.*?\|', data)  # 4
    print(Author)
    print(len(Author), len(Message), len(Date), len(Webaddress))
    alllist = []

    for i in range(len(Author)):
        dic = dict(Author=Author[i], Date=Date[i], Message=Message[i], webaddress=Webaddress[i], hour=hour[i])
        alllist.append(dic)
    print(alllist)
    return alllist
