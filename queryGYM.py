import requests
import bs4
from bs4 import BeautifulSoup
import urllib.request,json,urllib3,string
import xlrd,xlwt,xlutils.copy


global_city_list = []

def getHTMLText(url):                 #获取 html 源码
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url,headers=kv,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def queryHBAllCitys():          #先取到河北所有的县市区
    temp_city_list = []
    citylistURL = "http://www.56mp.com/statics/css/ditu/hebei2.htm"
    html = getHTMLText(citylistURL)
    soup = BeautifulSoup(html,"html.parser")
    for ele in soup.find_all('td',attrs={'width':"96%"}):
        if isinstance(ele,bs4.element.Tag):
            urllist = ele.find_all('a')
            for url in urllist:
                temp_city_list.append(url.text)


    rongcheng_index = temp_city_list.index('容城')
    rongchlist = temp_city_list #temp_city_list[rongcheng_index:]

    global_city_list = list(rongchlist)
    print('queryHBAllCity{}'.format(global_city_list))
    return  global_city_list


def queryOneCity(city_name):    #查询一个县市的体育场
    print(city_name)
    page_num = 0
    while True:
        one_page_result = queryOnePage(city_name,page_num) #查一页
        page_num += 1
        print(one_page_result)
        if one_page_result['total'] == 0:
            break

def queryOnePage(city_name,page_num):
    baiduurl = "http://api.map.baidu.com/place/v2/search?q=体育场&region={}&city_limit=true&output=json&ak=gCmXWaPd51zKcmaO3YAMjf4hVg7nhs6T&page_size=20&page_num={}".format(
        city_name,page_num)
    temp = urllib.request.urlopen(urllib.request.quote(baiduurl, safe=string.printable))
    body = temp.read()
    html = body.decode('utf-8')
    gymjson = json.loads(html)
    saveOnePage(city_name,gymjson['results'])
    return gymjson

def saveOnePage(city_name,result_diction):

    raw_work_book = xlrd.open_workbook('/Users/mac1/Desktop/GEMM3.xls')
    write_book = xlutils.copy.copy(raw_work_book)
    raw_sheet = raw_work_book.sheet_by_index(0)
    raw_data_rows = raw_sheet.nrows
    write_sheet = write_book.get_sheet(0)

    i = 0

    for one_gym in result_diction:
        if '体育' in one_gym['name']:
            write_sheet.write(raw_data_rows + i, 0, one_gym['name'])
            if 'address' in one_gym.keys():
                write_sheet.write(raw_data_rows + i, 1, one_gym['address'])
            else:
                write_sheet.write(raw_data_rows + i, 1, '没查到')
            if 'telephone' in one_gym.keys():
                write_sheet.write(raw_data_rows + i, 2, one_gym['telephone'])
            else:
                write_sheet.write(raw_data_rows + i, 2, '没查到')
            write_sheet.write(raw_data_rows + i, 3, city_name)
            i += 1

    write_book.save('/Users/mac1/Desktop/GEMM3.xls')

def main():
    allcityGYMinfo = []
    citylist = []
    citylistURL = "http://www.56mp.com/statics/css/ditu/hebei2.htm"
    queryHBAllCitys(citylistURL,citylist)
    for i in range(citylist):
        queryOneCity(citylist[i])


def test():
    rongcity = queryHBAllCitys()

    print('dieeieieieiei')
    print('test{}'.format(global_city_list))

    for city in rongcity:
        queryOneCity(city)



test()