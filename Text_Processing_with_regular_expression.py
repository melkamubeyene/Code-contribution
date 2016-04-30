import nltk
import string
import os
import re
import io
import codecs
import gensim
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
from gensim.models import ldamodel
os.chdir('/home/melkamu/parliament_corpus_2/en')
path = '/home/melkamu/parliament_corpus_2/fr-en/fr'
token_dict =[]
stemmer = PorterStemmer()
stoplist = set(nltk.corpus.stopwords.words("english")).union(set(nltk.corpus.stopwords.words("french")))
stemmed = []
for fn in os.listdir(path):
    fin = codecs.open(os.path.join(path, fn), 'r')
    text = fin.read()
    text1=re.sub("<.*?>",'',text)
    fin.close()
    fin = codecs.open(os.path.join(path, fn), 'w')
    fin.write(text1)
    fin.close()
