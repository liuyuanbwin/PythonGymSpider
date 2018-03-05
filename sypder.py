import requests
import bs4
import sklearn
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常" + r.status_code
if __name__ == "__main__":
    url = "https://www.amazon.cn/图书/dp/B01M8L5Z3Y/ref=sr_1_1?ie=UTF8&qid=1494831477&sr=8-1&keywords=极简"
    print(getHTMLText(url))