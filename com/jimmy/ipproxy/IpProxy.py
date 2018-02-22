import requests
from lxml import etree
from os.path import exists, getsize, dirname, abspath

HTTP_IP_LIST = "ip_list_http.txt"

# 获取当前文件所在的目录,然后得到需要文件的绝对路径
HTTP_IP_LIST_PATH = dirname(abspath(__file__)) + "/" + HTTP_IP_LIST
print('path:', HTTP_IP_LIST_PATH)


def write_file_by_line(filename, data_list):
    file = open(filename, "w")
    for i in range(len(data_list)):
        file.write(data_list[i])
        file.write("\n")
    file.close()
    return


def get_ip_list(response):
    """
    https://zhuanlan.zhihu.com/p/29436838
    :param response:
    :return:
    """
    ip_list_xml = etree.HTML(response)
    ip_list = ip_list_xml.xpath('//tr/td[2]/text()')
    port_list = ip_list_xml.xpath('//tr/td[3]/text()')
    type_list = ip_list_xml.xpath('//tr/td[6]/text()')
    print("ip_list len : " + str(len(ip_list)) + " port_list len : " + str(len(port_list)))

    nn_list = []
    for i in range(len(ip_list)):
        # 如果代理是80端口的话,应该是被有道劫持了,所以过滤掉80端口的代理
        if type_list[i] == "HTTP" and int(port_list[i]) != int(80):
            nn_list.append(str(ip_list[i]) + ":" + str(port_list[i]))
    return nn_list


def refresh_proxy_list():
    # 代理列表 http://www.xicidaili.com/
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

    url = 'http://www.xicidaili.com/nn/'

    if (not exists(HTTP_IP_LIST_PATH)) or getsize(HTTP_IP_LIST_PATH) == 0:
        print("ip list is null")
        response = requests.get(url, headers=headers, timeout=3).text
        ip_list = get_ip_list(response)
        write_file_by_line(HTTP_IP_LIST_PATH, ip_list)
        return

    file = open(HTTP_IP_LIST_PATH)

    for line in file.readlines():
        ip_proxy = 'http://' + line.strip()
        proxies = {
            "http": ip_proxy,
            # "http": "http://106.112.160.134:808",
        }
        try:
            response = requests.get(url, headers=headers, proxies=proxies, timeout=3).text
            ip_list = get_ip_list(response)
            if len(ip_list) > 0:
                write_file_by_line(HTTP_IP_LIST_PATH, ip_list)
                print("get ip list is ok.")
            break
        except Exception as e:
            print('get ip list is exception, proxy ', ip_proxy, " is error.")

    file.close()

# refresh_proxy_list()
