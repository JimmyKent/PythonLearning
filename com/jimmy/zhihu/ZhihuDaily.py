import requests
import json
from com.jimmy.ipproxy import IpProxy


class ZhihuList:
    def __init__(self, date, stories):
        self.date = date
        self.stories = stories


if __name__ == '__main__':

    IpProxy.refresh_proxy_list()
    file = open(IpProxy.HTTP_IP_LIST_PATH)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

    url = 'http://news.at.zhihu.com/api/4/news/before/20180220'
    res = ""
    for line in file.readlines():
        ip_proxy = 'http://' + line.strip()
        print("get zhihu content ip_proxy is ", ip_proxy)
        proxies = {
            "http": ip_proxy,
            # "http": "http://106.112.160.134:808",
        }
        try:
            res = requests.get(url, headers=headers, proxies=proxies, timeout=3).text
            print(res)
            if "date" in res:
                break
        except Exception as e:
            print("get zhihu content is exception, proxy is error")

    if "date" in res:
        file = open("zhihu_json.txt", "wb")
        file.write(res.encode("utf-8"))
        file.close()

    file.close()

