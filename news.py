import urllib.request
import re
import chardet
from urllib.parse import urlparse
from urllib import parse

class ha(object):

    def newsList(self) -> None:
              
        newsListDo = [] 
        url = 'https://news.google.com/?hl=zh-TW&gl=TW&ceid=TW:zh-Hant'
        google_url = 'https://news.google.com/'
        titleText = re.compile(r'<h[3-4] class="ipQwMb ekueJc RD0gLb"><a .*?>(.*?)</a><')
        linkText = re.compile(r'<h[3-4] class="ipQwMb ekueJc RD0gLb"><a href="([^">]+?)"')
        mediaText = re.compile(r'<a .*? class="wEwyrc AVN2gc uQIVzc Sksgp">(.*?)</a>')

        html = urllib.request.urlopen(url).read()
        encode_type = chardet.detect(html)
        html = html.decode(encode_type['encoding'])
        
        titleh3 = re.findall(titleText, html)
        linkh3 = re.findall(linkText, html)
        mediaNameList = re.findall(mediaText, html)

        x=0
        for i in range(0,len(titleh3)):
            link = parse.urljoin(google_url , linkh3[i])
            newsListDo.append(crawlerSingleNews(str(x),titleh3[i],link))
            x+=1
        
        return newsListDo


class crawlerSingleNews(object):
    
    def __init__(self, id: str,title: str,link: str)-> None:
        self.id = id
        self.title = title
        self.link = link
   
result = ha().newsList()