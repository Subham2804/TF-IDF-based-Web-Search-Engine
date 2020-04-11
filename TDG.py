
import urllib.request, urllib.error, urllib.parse
import os
import bleach
from bs4 import BeautifulSoup
import tagrem
from tfidf import TfIdf
from nltk.tokenize import  word_tokenize
from nltk.stem import WordNetLemmatizer


def index(urls):
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

def word_preprocessing(list):
    lemmatizer = WordNetLemmatizer() 

    for i in list:
        i.lower()
        lemmatizer.lemmatize(i)
    return list    





if __name__ =="__main__":
    urls=input().strip().split()
    index(urls)
    l1=[]
    l2=tagrem.text_parser(urls,l1)
    query=input().strip().split()
    query=word_preprocessing(query)
    table = TfIdf()
    for i in range(len(urls)):
        table.add_document(str(i),l2[i])
    x=table.similarities(query) 
    for i in x:
        print(x[0])   


    