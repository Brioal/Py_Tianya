from tianya import UrlManager, Downloader, Parser, Writer


class Main(object):

    def __init__(self):
        self.urls = UrlManager.Manager()
        self.downloader = Downloader.Downloader()
        self.parser = Parser.Parser()
        self.writer = Writer.Writer()

    # 抓取目录
    def crawMenu(self):
        self.urls.add_menu('/list-16-1.shtml')
        f = open('menus.txt', 'w')
        f.close()
        while self.urls.has_new():
            url = self.urls.get_new()
            # 获取网页内容
            content = self.downloader.download(url)
            # 获取下一页地址
            url = self.parser.get_next_url(content)
            # 添加下一页地址
            self.urls.add_menu(url)
            # 解析目录
            menus = self.parser.parserMenu(content)
            # 写到文件里面
            self.writer.writeMenus(menus)


if __name__ == "__main__":
    spider = Main()
    spider.crawMenu()
