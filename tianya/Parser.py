from bs4 import BeautifulSoup
import re


class Parser(object):
    # 解析目录
    def parserMenu(self, content):
        if content is None:
            return
        soup = BeautifulSoup(content, 'html')
        menus = self.__get_menus(soup)
        return menus

    # 获取下一页的地址
    def get_next_url(self, content):
        if content is None:
            return
        soup = BeautifulSoup(content, 'html')
        # href="/list.jsp?item=16&nextid=1554822262000"
        next_a = soup.find_all('a', href=re.compile(r"/list.jsp\?item=16&nextid=.+"))
        if next_a is None:
            print('没有下一页了')
            return None
        next_url = next_a[0]['href']
        print('下一页地址:', next_url)
        return next_url

    # 获取目录列表
    def __get_menus(self, soup):
        menus = []
        trs = soup.find_all('tr')
        # 循环,获取标题,作者,阅读量,地址,回复,更新时间
        for tr in trs:
            data = {}
            # 获取标题
            title_a = tr.find('a')
            if title_a is None:
                continue
            # print(title_a)
            title = title_a.get_text()
            # 去除换行
            title = title.replace("\t", "")
            title = title.replace("\n", "")
            title = title.replace("\r", "")
            print(title)
            data['title'] = title
            # 获取作者
            author_a = tr.find('a', class_='author')
            if author_a is None:
                continue
            # print(author_a)
            author = author_a.get_text()
            # print(author)
            data['author'] = author
            # 获取阅读量
            td_arrar = tr.find_all('td')
            # print(td_arrar)
            if len(td_arrar) < 5:
                continue
            read_a = td_arrar[2]
            # print(read_a)
            read = read_a.get_text()
            data['read'] = read
            # print(read)
            # 获取回复数量
            review_a = td_arrar[3]
            # print(review_a)
            review = review_a.get_text()
            data['review'] = review
            # print(review)
            # 获取更新时间
            time_a = td_arrar[4]
            # print(time_a)
            time = time_a.get_text()
            # print(time)
            data['time'] = time

            print(data)
            menus.append(data)

        return menus
