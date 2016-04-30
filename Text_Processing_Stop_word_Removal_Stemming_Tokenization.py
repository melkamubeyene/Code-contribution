import nltk
import string
import os
import re
import io
import codecs
import gensim
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from gensim import corpora, models
from gensim.models import ldamodel
pathen= '/home/sciencelib/Desktop/Melkamu_Data/test_data/Test_engwiki'#path for english text
pathfr = '/home/sciencelib/Desktop/Melkamu_Data/test_data/testfrenchwiki'#path for french text
stemmeren =PorterStemmer()#Stemmer for english text
stemmerfr =SnowballStemmer("french",ignore_stopwords=True)#Stemmer for french text
stoplisten = set(nltk.corpus.stopwords.words("english"))#english stop_word list
stoplistfr = set(nltk.corpus.stopwords.words("french"))#french stop_word list
for fn in os.listdir(pathen):
    fin = codecs.open(os.path.join(pathen, fn), 'r')
    text = fin.read()
    fin.close()
    text2=[x for x in gensim.utils.tokenize(text, lowercase=True, deacc=True, errors="ignore") if not x in stoplisten]
    fin = codecs.open(os.path.join(pathen, fn), 'w')
    text3=[stemmeren.stem(y)for y in text2]
    fin.write(str(text3))
    fin.close()
