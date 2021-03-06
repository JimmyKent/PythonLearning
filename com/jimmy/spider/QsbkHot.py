# -*- coding:utf-8 -*-

"""

现在正则表达式在这里稍作说明

1）.*? 是一个固定的搭配，.和*代表可以匹配任意无限多个字符，加上？表示使用非贪婪模式进行匹配，也就是我们会尽可能短地做匹配，以后我们还会大量用到 .*? 的搭配。

2）(.*?)代表一个分组，在这个正则表达式中我们匹配了五个分组，在后面的遍历item中，item[0]就代表第一个(.*?)所指代的内容，item[1]就代表第二个(.*?)所指代的内容，以此类推。

3）re.S 标志代表在匹配时为点任意匹配模式，点 . 也可以代表换行符。

"""

__author__ = 'Jimmy'

import urllib.request as urllib2
import re
import sqlite3


def get_qsbk_list(page):
    if page < 1:
        page = 1
    url = 'https://www.qiushibaike.com/hot/page/' + str(page)
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    _list = []
    try:
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
        # print(content)

        pattern = re.compile('<span>(.*?)</span>', re.S)
        items = re.findall(pattern, content)
        for item in items:
            # print(item.strip())
            _list.append(item.strip())

    except urllib2.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return _list


def filter_list():
    pass


def create_db(db_name):
    # 连接到SQLite数据库
    # 数据库文件是test.db
    # 如果文件不存在，会自动在当前目录创建:
    conn = sqlite3.connect(db_name)
    # 创建一个Cursor:
    cursor = conn.cursor()
    # 执行一条SQL语句，创建user表:
    cursor.execute('create table if not exists hot (id integer primary key autoincrement, joke text)')


def save_to_db(_list):
    conn = sqlite3.connect('qsbk.db')
    # 创建一个Cursor:

    # 继续执行一条SQL语句，插入一条记录:
    for joke in _list:
        if "\'" not in joke:
            cursor = conn.cursor()
            cursor.execute('insert into hot (joke) values (\'' + str(joke) + '\')')
            cursor.close()
            conn.commit()
    # cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
    # 关闭Cursor:

    # 提交事务:

    # 关闭Connection:
    conn.close()


def query():
    conn = sqlite3.connect('qsbk.db')
    cursor = conn.cursor()
    # 执行查询语句:
    cursor.execute('select * from hot')
    # 获得查询结果集:
    values = cursor.fetchall()
    for joke in values:
        print(joke)
    cursor.close()
    conn.close()


def query_size():
    conn = sqlite3.connect('qsbk.db')
    cursor = conn.cursor()
    cursor.execute("Select * from hot;")
    print(cursor.__sizeof__())
    cursor.close()
    conn.close()


if __name__ == "__main__":
    print("this is program entrance")
    create_db('qsbk.db')
    for i in range(1, 10):
        hot_list = get_qsbk_list(i)
        print(hot_list.__sizeof__())
        save_to_db(hot_list)
    # query()
    query_size()
