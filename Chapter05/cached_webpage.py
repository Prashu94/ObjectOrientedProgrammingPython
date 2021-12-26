from urllib.request import urlopen

class WebPage:
    def __init__(self, url):
        self.url = url
        self._content = None

    def content(self):
        if not self._content:
            print("Retrieving New Page...")
            self._content = urlopen(self.url).read()
        return self._content

if __name__=="__main__":
    import time
    webpage = WebPage("http://ccphillps.net/")
    now = time.time()
    content1 = webpage.content
    print(time.time() - now)
    now = time.time()
    content2 = webpage.content
    print(time.time()-now)
    print(content2 == content1)