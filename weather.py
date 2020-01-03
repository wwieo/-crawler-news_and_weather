import request
import time
from bs4 import BeautifulSoup, Tag
from flask import Flask, request, abort
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
import urllib.request
import re
import chardet
from urllib.parse import urlparse
from urllib import parse

class ha(object):

    def newsList(self) -> None:
              
        weatherListDo = []
        area = []
        weather = []

        url='https://www.cwb.gov.tw/V8/C/W/County/MOD/wf7dayNC_NCSEI/ALL_Week.html'
        html = urllib.request.urlopen(url).read()
        encode_type = chardet.detect(html)
        html = html.decode(encode_type['encoding'])  
        soup = BeautifulSoup(html, 'html.parser')

        for i in soup.select('.heading_3'):
            if(i.string is not None)and(i.string != "縣市"):
                area.append(i.string)
                print(i.string)

        x = 1
        for i in soup.find_all('span', attrs={'class': "signal"}):
            if x % 14 == 1:
                weather.append(i.find('img').get('alt'))
                print(i.find('img').get('alt'))
            x+=1

        return weatherListDo               

   
ha().newsList()