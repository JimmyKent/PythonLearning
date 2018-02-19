import requests
from lxml import etree


def write_file_by_line(filename, data_list):
    file = open(filename, "w")
    for i in range(len(data_list)):
        file.write(data_list[i])
        file.write("\n")
    file.close()
    return


def get_ip_list(response):
    ip_list_xml = etree.HTML(response)
    ip_list = ip_list_xml.xpath('//tr/td[2]/text()')
    port_list = ip_list_xml.xpath('//tr/td[3]/text()')
    type_list = ip_list_xml.xpath('//tr/td[6]/text()')
    print("ip_list len : " + str(len(ip_list)) + " port_list len : " + str(len(port_list)))

    nn_list = []
    for i in range(len(ip_list)):
        if type_list[i] == "HTTP":
            nn_list.append(str(ip_list[i]) + ":" + str(port_list[i]))
    return nn_list


if __name__ == '__main__':
    # 代理列表 http://www.xicidaili.com/
    proxies = {
        "http": "http://111.155.116.238:8123",
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

    url = 'http://www.xicidaili.com/nn/'
    response = requests.get(url, headers=headers, proxies=proxies).text
    print("-----response-----")
    print(response)
    print("-----response end -----")
    ip_list = get_ip_list(response)
    write_file_by_line("ip_text.txt", ip_list)
