class Writer(object):
    # 将目录写到文件里面
    def writeMenus(self, menus):
        f = open('menus.txt','a',encoding='utf-8')
        for data in menus:
            f.write(data['title']+"[]"+data['author']+'[]'+data['read']+"[]"+data['review']+"[]"+data['time'])
            f.write('\r')
        f.close()