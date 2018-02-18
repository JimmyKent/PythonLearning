import requests

# 代理列表 http://www.xicidaili.com/
proxies = {

    "http": "http://121.227.116.115:3128",
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

url = 'http://daily.zhihu.com/'
res = requests.get(url, headers=headers, proxies=proxies).text
# print(len(res))

print(res)
