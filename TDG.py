
import urllib.request, urllib.error, urllib.parse
import os
import bleach
from bs4 import BeautifulSoup
import tagrem

from nltk.tokenize import  word_tokenize

def Downloader(urls):
    for i in range(len(urls)):
        url=urls[i]
        response = urllib.request.urlopen(url)
        webContent = response.read()
        file=os.getcwd()+"/webpages/file"+str(i)+".html"
        if not os.path.exists(os.getcwd()+"/webpages"):
            os.mkdir(os.getcwd()+"/webpages")
        f = open(file, 'wb')
        f.write(webContent)
        f.close





if __name__ =="__main__":
    urls=input().strip().split()
    Downloader(urls)
    tagrem.text_parser(urls)