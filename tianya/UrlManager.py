class Manager(object):

    def __init__(self):
        self.menus = set()

    # 添加菜单地址
    def add_menu(self, url):
        if url is None:
            return
        # 添加下一页地址 1
        url = 'http://bbs.tianya.cn' + url
        self.menus.add(url)

    # 　是否有地址
    def has_new(self):
        return len(self.menus) != 0

    # 获取一个地址
    def get_new(self):
        url = self.menus.pop()
        return url
