import requests
from requests.exceptions import ProxyError

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
            res = requests.get(url, headers=headers, proxies=proxies, timeout=10).text
            print(res)
            if "date" in res:
                zhihu_proxy = ip_proxy
                break
        except ProxyError:
            print("get zhihu content is exception, proxy is error")

    if "date" in res:
        zhihu_daily_dir = "zhihu_daily_" + str(date)
        try:
            os.makedirs(zhihu_daily_dir)
        except OSError:
            print(zhihu_daily_dir + " is exist")
        file = open(zhihu_daily_dir + "/zhihu_daily_list_" + str(date) + ".txt", "wb")
        file.write(res.encode("utf-8"))
        file.close()

    proxy_file.close()


def parse_zhihu_daily_list_json(zhihu_daily_list_str):
    """
    解析返回的json
    :param zhihu_daily_list_str: 原始数据
    :return:
    """
    # 将 JSON 对象转换为 Python 字典
    zhihu_daily_json = json.loads(zhihu_daily_list_str)
    # print("zhihu_daily_json['date']: ", zhihu_daily_json['date'])
    stories_list = zhihu_daily_json['stories']
    # print(stories_list)  # 获取列表内容
    return stories_list


def get_zhihu_daily_article_and_save(date, article_list):
    zhihu_daily_dir = "zhihu_daily_" + str(date)
    for i in range(len(article_list)):
        print()

        print(article_list[i])  # 获取第一项
        # 获取文章id
        article_id = article_list[i]["id"]
        print(article_id)
        # 获取文章title
        article_title = article_list[i]["title"]
        print(article_title)

        proxy_file = open(IpProxy.IP_LIST_HTTP_PATH)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

        url = 'http://news-at.zhihu.com/api/4/news/' + str(article_id)
        res = ""
        try:
            res = requests.get(url, headers=headers, proxies=zhihu_proxy, timeout=10).text
            print("article detail ", res)
        except ProxyError:
            print("get zhihu detail is exception, proxy is error")

        # 将 JSON 对象转换为 Python 字典
        zhihu_detail_json = json.loads(res)
        # print("zhihu_daily_json['date']: ", zhihu_daily_json['date'])
        zhihu_detail_body = zhihu_detail_json['body']
        file = open(zhihu_daily_dir + "/" + article_title + ".txt", "wb")
        file.write(zhihu_detail_body.encode("utf-8"))
        file.close()

        # for line in proxy_file.readlines():
        #     ip_proxy = 'http://' + line.strip()
        #     print("get zhihu content ip_proxy is ", ip_proxy)
        #     proxies = {
        #         "http": ip_proxy,
        #         # "http": "http://106.112.160.134:808",
        #     }
        #     try:
        #         res = requests.get(url, headers=headers, proxies=proxies, timeout=3).text
        #         print(res)
        #         if "date" in res:
        #             break
        #     except ProxyError:
        #         print("get zhihu content is exception, proxy is error")


if __name__ == '__main__':
    IpProxy.refresh_proxy_list()
    date = 20180220
    zhihu_proxy = ""
    get_zhihu_daily_list(date)
    file = open("zhihu_daily_20180220/zhihu_daily_list_20180220.txt", "r", encoding="utf-8")
    zhihu_daily_list_str = file.read()
    # print(zhihu_daily_str)
    stories_list = parse_zhihu_daily_list_json(zhihu_daily_list_str)
    get_zhihu_daily_article_and_save(date, stories_list)
