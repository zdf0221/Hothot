# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test
   Description :
   Author :       zdf's desktop
   date：          2020/6/16
-------------------------------------------------
   Change Activity:
                   2020/6/16:20:45
-------------------------------------------------
"""

import requests, html5lib
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gb2312;utf-8",
    "Connection": "keep-alive",
}


if __name__ == "__main__":
    item_name = "仙女的泪水"
    # print(item_name)
    url = "http://canto.world-of-dungeons.org/wod/spiel/hero/item.php?name={}".format(item_name)
    req = requests.get(url, headers=headers, )
    html = req.content
    html = str(html, 'utf-8')  # Same as: html_doc=html.decode("utf-8","ignore")
    soup = BeautifulSoup(html, features='html5lib')
    # print(soup.prettify())
    item_name = str(soup.title.string)[4:-20:]  # strip title tag
    # print(item_name)

    spec = soup.find(id='details')
    # spec = soup.find_all('td')
    # print(spec.text)
    detail = spec.text.replace(' ', '').strip()
    detail = detail.split("\t")
    detail = [c for c in detail if c]
    detail = [c for c in detail if c != '\n']
    detail = [c for c in detail if c != '\n\n']
    ans = []
    for s in detail:
        s = s.strip('\n')
        ans.append(s)
    detail = ans
    # print(detail)
    attribute = soup.find(id='link')
    attribute = attribute.text.replace(' ', '').strip()
    attribute = attribute.split("\t")
    attribute = [c for c in attribute if c]
    attribute = [c for c in attribute if c != '\n']
    attribute = [c for c in attribute if c != '\n\n']
    attribute = [c for c in attribute if c != '\n\n\n']
    attribute = [c for c in attribute if c != '\n\n\n\n']
    attribute = [c for c in attribute if c != '\n\n\n\n\n']
    ans = []
    for s in attribute:
        s = s.replace('\n', ' ')
        ans.append(s)
    attribute = ans
    # print(attribute)
    ans = detail + attribute
    print(ans)






