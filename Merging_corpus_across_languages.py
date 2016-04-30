import codecs
import scipy.sparse
from pattern.vector import Document, Model,TFIDF, Corpus
import sys
import os
import pandas as pd
from collections import defaultdict
from sklearn.decomposition import TruncatedSVD
from sklearn.random_projection import sparse_random_matrix
from sklearn.metrics.pairwise import cosine_similarity
from numpy import linalg
import scipy
import scipy.sparse
import sklearn
from collections import defaultdict
import nltk
from nltk.tokenize import sent_tokenize
import string
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
from gensim.models import ldamodel
import filecmp
import glob
path= '/home/melkamu/parliament_corpus/english'
pathen ='/home/melkamu/parliament_corpus/french'
for fn in os.listdir(path):
    for fn1 in os.listdir(pathen):
        fin = open(os.path.join(path, fn), 'a+')
        fin1 = open(os.path.join(pathen, fn1), 'r')
        text=fin1.read()
        if fn==fn1:
            fin.write(text)
            fin.close()
