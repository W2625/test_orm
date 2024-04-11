import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        # 通过get函数获取url，并设定了timeout时间是30秒
        r = requests.get(url,timeout = 30)
        # raise_for_status产生异常信息
        r.raise_for_status()
        # 修改编码
        r.encoding = r.apparent_encoding()
        # 返回网页内容
        return r.text
    except:
        # 出现错误返回空字符串
        return ""

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        # 检测tr标签的类型过滤掉非标签类型的其他信息
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append(tds[0].string,tds[1].string,tds[2].string,tds[3].stringtds[4].string,tds[5].string)

def printUnivList(ilist, num):
    print({:^6}\t{:^6}\t{:^6}\t{:^6}\t{:^10}.format("2023排名","2022排名","全部层次","学校名称","总分"))
    for i in range(num):
        u = ulist[i]
        print({:^6}\t{:^6}\t{:^6}\t{:^6}\t{:^10}.format(u[0],u[1],u[2],u[3],u[4]))


def main():
    uinfo = []
    url = "https://www.shanghairanking.cn/rankings/bcsr/2023/0835"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)    # 20 univs

main()

