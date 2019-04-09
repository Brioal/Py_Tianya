import urllib.request
import urllib.response


class Downloader(object):
    # 下载网页
    def download(self, url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)
        code = response.status
        print(code)
        if code != 200:
            return None
        content = response.read()
        print(content)
        return content
