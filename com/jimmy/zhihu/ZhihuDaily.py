import requests
from com.jimmy.ipproxy import IpProxy
import os
import json


def get_zhihu_daily_list(date):
    """
    获取某天的知乎日报列表
    http://news.at.zhihu.com/api/4/news/before/20180220
    :param date: 20180220
    :return: json
    """
    proxy_file = open(IpProxy.IP_LIST_HTTP_PATH)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

    url = 'http://news.at.zhihu.com/api/4/news/before/' + str(date)
    res = ""
    for line in proxy_file.readlines():
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
        zhihu_daily_dir = "zhihu_daily_" + str(date)
        try:
            os.makedirs(zhihu_daily_dir)
        except OSError as e:
            print(zhihu_daily_dir + " is exist")
        file = open(zhihu_daily_dir + "/zhihu_daily_list_" + str(date) + ".txt", "wb")
        file.write(res.encode("utf-8"))
        file.close()

    proxy_file.close()


if __name__ == '__main__':
    IpProxy.refresh_proxy_list()
    get_zhihu_daily_list(20180220)

