import requests

if __name__ == '__main__':

    file = open("../ipproxy/ip_text.txt")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

    url = 'http://daily.zhihu.com/'

    for line in file.readlines():
        ip_proxy = 'http://' + line.strip()
        proxies = {
            "http": ip_proxy,
            # "http": "http://106.112.160.134:808",
        }
        try:
            res = requests.get(url, headers=headers, proxies=proxies, timeout=3).text
            print(ip_proxy)
            print(res)
        except Exception as e:
            print('Error:')

    file.close()
