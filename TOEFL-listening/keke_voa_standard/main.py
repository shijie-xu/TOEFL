# -*- coding:utf-8 -*-

import tkinter
import re
import urllib
import urllib.request
import requests
import sys


def get_homepage(url):
    html = requests.get(url).text
    return html


def get_items(html):
    pattern = re.compile(
        r'<a href="(http://.+?)" title=".+?" target="_blank">.+?</a>')
    return re.findall(pattern, html)


if __name__ == '__main__':
    homepage_url = r'http://www.kekenet.com/broadcast/Normal/'
    html = get_homepage(homepage_url)
    items = get_items(html)
    for url in items:
        # get news homepage
        content = get_homepage(url)
        # get title
        pattern_title = re.compile(
            r'<h1 id="nrtitle">(.+?)</h1>')
        title = re.findall(pattern_title, content)[0]

        # get mp3
        pattern_mp3 = re.compile(
            r'<a target="_blank" href="(.+?)"><font color="blue">下载MP3到电脑</font></a>'
        )
        # print(content)
        mp3_page = re.findall(pattern_mp3, content)[0]
        mp3_content = get_homepage(r'http://www.kekenet.com/'+mp3_page)

        pattern_downmp3 = re.compile(
            r'<a target="_blank" href="(.+?)" style="color:#195A94;"><font size="5px"><strong>mp3下载地址1</strong></font></a>'
        )
        mp3_link = re.findall(pattern_downmp3, mp3_content)[0]
        urllib.request.urlretrieve(mp3_link, title+".mp3")
