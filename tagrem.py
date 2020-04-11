import urllib.request
from nltk.tokenize import  word_tokenize
from nltk.corpus import stopwords 
from nltk.stem import WordNetLemmatizer
import pickle 
import os
from bs4 import BeautifulSoup
def text_parser(urls,l):
        lemmatizer = WordNetLemmatizer() 

        for i in range(len(urls)):

                html = urllib.request.urlopen(urls[i]).read()
                soup = BeautifulSoup(html,features="lxml")

# kill all script and style elements
                for script in soup(["script", "style"]):
                        script.extract()    # rip it out

# get text
                text = soup.get_text()

# break into lines and remove leading and trailing space on each
                lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
                chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
                text = '\n'.join(chunk for chunk in chunks if chunk)
        
                tokens=word_tokenize(text)
                x= [lemmatizer.lemmatize(w.lower()) for w in tokens if not w in stopwords.words('english')]
                l.append(x)
        return l        