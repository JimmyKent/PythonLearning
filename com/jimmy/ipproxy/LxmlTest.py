from lxml import etree


# 定义一个函数，给他一个html，返回xml结构
def getxpath(html):
    return etree.HTML(html)


# test
sample1 = """<html>
  <head>
    <title>My page</title>
  </head>
  <body>
    <h2>Welcome to my <a href="#" src="x">page</a></h2>
    <p>This is the first paragraph.</p>
    <!-- this is the end -->
  </body>
</html>
"""
# 获取xml结构
s1 = getxpath(sample1)

# 获取标题(两种方法都可以)
s2 = s1.xpath('//title/text()')
s3 = s1.xpath('/html/head/title/text()')

# print(s2)
# print(s3)

file = open("IpListDemo.txt", "r", encoding="utf-8")
fileStr = ""
for line in file.readlines():
    fileStr += line

# print(fileStr)
ipListXml = getxpath(fileStr)
ip = ipListXml.xpath('//tr')
ipClass = ipListXml.xpath('//tr/@class')
# print(ip)
# print(len(ip))
# print(type(ip))
# print(type(ip[0]))
# print(ipClass)
# print(len(ipClass))
ip1 = ipListXml.xpath('//tr/td[2]/text()')
print(ip1)
# html = etree.parse('IpListDemo.txt')
# result = html.xpath('//td')
# print(result)
# print(len(result))
# print(type(result))
# print(type(result[0]))
"""
<tr class="odd">
      <td class="country"><img src="http://fs.xicidaili.com/images/flag/cn.png" alt="Cn" /></td>
      <td>125.113.103.97</td>
      <td>8118</td>
      <td>
        <a href="/2018-02-17/zhejiang">浙江金华</a>
      </td>
      <td class="country">高匿</td>
      <td>HTTPS</td>
      <td class="country">
        <div title="0.386秒" class="bar">
          <div class="bar_inner fast" style="width:87%">
            
          </div>
        </div>
      </td>
      <td class="country">
        <div title="0.077秒" class="bar">
          <div class="bar_inner fast" style="width:99%">
            
          </div>
        </div>
      </td>
      
      <td>15小时</td>
      <td>18-02-18 15:11</td>
    </tr>
"""
