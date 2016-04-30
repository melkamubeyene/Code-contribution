import logging
import codecs
import os
import io
import gensim
from gensim import corpora, models
from gensim.models import ldamodel
def iter_docs(topdir, stoplist):
    for fn in os.listdir(topdir):
        fin = codecs.open(os.path.join(topdir, fn), 'rb')
        text = fin.read()
        fin.close()
        yield (x for x in 
            gensim.utils.tokenize(text, lowercase=True, deacc=True, errors="ignore")
            if x not in stoplist)
class MyCorpus(object):
    def __init__(self, topdir, stoplist):
        self.topdir = topdir
        self.stoplist = stoplist
        self.dictionary = gensim.corpora.Dictionary(iter_docs(topdir, stoplist))
    def __iter__(self):
        for tokens in iter_docs(self.topdir, self.stoplist):
            yield self.dictionary.doc2bow(tokens)
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
TEXTS_DIR = ''#this is the path for the training or testing data corpus
MODELS_DIR = ''#this is the path for saving preprocessed documents 
stoplist = set([])
corpus = MyCorpus(TEXTS_DIR, stoplist)
corpus.dictionary.save(os.path.join(MODELS_DIR, "test_from_french_wiki.dict"))
gensim.corpora.MmCorpus.serialize(os.path.join(MODELS_DIR, "test_from_french_wiki.mm"), corpus)
corpus = corpora.MmCorpus('/home/sciencelib/Desktop/Melkamu_Data/model_final_200/test_set/test_from_french_wiki.mm')#loading the corpus
model = ldamodel.LdaModel(corpus, num_topics=200)#the model 
