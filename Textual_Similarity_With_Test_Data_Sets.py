import gensim
from gensim import corpora, models
from gensim.models import ldamodel
import numpy as np
#Loading the Bi-lingual LDA model 
def model(path):
    model=models.LdaModel.load(path)
    return model
#Preprocessing the Test Corpus for the model
def test_corpus(path):
    corpus = corpora.MmCorpus(path)
    return corpus
model=model('/home/sciencelib/Desktop/Melkamu_Data/model_final_200/modelfinal.lda')#path for the model
testen=test_corpus('/home/sciencelib/Desktop/Melkamu_Data/model_final_200/test_set/test_from_eng_wiki.mm')#path for test corpus extracted from english wikipedia
testfr=test_corpus('/home/sciencelib/Desktop/Melkamu_Data/model_final_200/test_set/test_from_french_wiki.mm')#path for test corpus extracted from french wikipedia
LDa_spaceen=model[testen]#Projecting the Test Corpus extracted from english wikipedia to the model
LDa_spacefr=model[testfr]#Projecting the Test Corpus extracted from french wikipedia to the model
test_doc_listen=[]#An empty list to hold test instances for english
test_doc_listfr=[]#An empty list to hold test instances for french
#Appending projected test documents 
for x in range(len(LDa_spaceen)):
    doc1=gensim.matutils.sparse2full(LDa_spaceen[x], model.num_topics)
    test_doc_listen.append(doc1)
for x in range(len(LDa_spacefr)):
    doc1=gensim.matutils.sparse2full(LDa_spacefr[x], model.num_topics)
    test_doc_listfr.append(doc1)
#Textual Similarity Computation
a=1-(np.sqrt(0.5 * ((np.sqrt(test_doc_listen[3]) - np.sqrt(test_doc_listen[5]))**2).sum()))
b=1-(np.sqrt(0.5 * ((np.sqrt(test_doc_listen[3]) - np.sqrt(test_doc_listen[7]))**2).sum()))
c=1-(np.sqrt(0.5 * ((np.sqrt(test_doc_listen[3]) - np.sqrt(test_doc_listfr[2]))**2).sum()))
d=1-(np.sqrt(0.5 * ((np.sqrt(test_doc_listen[3]) - np.sqrt(test_doc_listfr[3]))**2).sum()))
e=1-(np.sqrt(0.5 * ((np.sqrt(test_doc_listen[3]) - np.sqrt(test_doc_listfr[4]))**2).sum()))
f=1-(np.sqrt(0.5 * ((np.sqrt(test_doc_listen[3]) - np.sqrt(test_doc_listfr[5]))**2).sum()))
list382=[a,b,c,d,e,f]#The textual similarity of the entity 382 with candidate instances  
g=1-(np.sqrt(0.5 * ((np.sqrt(test_doc_listen[0]) - np.sqrt(test_doc_listfr[1]))**2).sum()))
h=1-(np.sqrt(0.5 * ((np.sqrt(test_doc_listen[0]) - np.sqrt(test_doc_listfr[10]))**2).sum()))
i=1-(np.sqrt(0.5 * ((np.sqrt(test_doc_listen[0]) - np.sqrt(test_doc_listen[5]))**2).sum()))
j=1-(np.sqrt(0.5 * ((np.sqrt(test_doc_listen[0]) - np.sqrt(test_doc_listfr[4]))**2).sum()))
k=1-(np.sqrt(0.5 * ((np.sqrt(test_doc_listen[0]) - np.sqrt(test_doc_listfr[9]))**2).sum()))
list381=[g,h,i,j,k]#The textual similarity of the entity 381 with candidate instances  
l=1-(np.sqrt(0.5 * ((np.sqrt(test_doc_listen[8]) - np.sqrt(test_doc_listen[2]))**2).sum()))
m=1-(np.sqrt(0.5 * ((np.sqrt(test_doc_listen[8]) - np.sqrt(test_doc_listfr[5]))**2).sum()))
n=1-(np.sqrt(0.5 * ((np.sqrt(test_doc_listen[8]) - np.sqrt(test_doc_listfr[0]))**2).sum()))
o=1-(np.sqrt(0.5 * ((np.sqrt(test_doc_listen[8]) - np.sqrt(test_doc_listfr[4]))**2).sum()))
p=1-(np.sqrt(0.5 * ((np.sqrt(test_doc_listen[8]) - np.sqrt(test_doc_listfr[6]))**2).sum()))
q=1-(np.sqrt(0.5 * ((np.sqrt(test_doc_listen[8]) - np.sqrt(test_doc_listfr[7]))**2).sum()))
list390=[l,m,n,o,p,q]#The textual similarity of the entity 390 with candidate instances
r=1-(np.sqrt(0.5 * ((np.sqrt(test_doc_listfr[11]) - np.sqrt(test_doc_listen[7]))**2).sum()))
s=1-(np.sqrt(0.5 * ((np.sqrt(test_doc_listfr[11]) - np.sqrt(test_doc_listen[13]))**2).sum()))
t=1-(np.sqrt(0.5 * ((np.sqrt(test_doc_listfr[11]) - np.sqrt(test_doc_listen[11]))**2).sum()))
u=1-(np.sqrt(0.5 * ((np.sqrt(test_doc_listfr[11]) - np.sqrt(test_doc_listfr[5]))**2).sum()))
v=1-(np.sqrt(0.5 * ((np.sqrt(test_doc_listfr[11]) - np.sqrt(test_doc_listfr[8]))**2).sum()))
w=1-(np.sqrt(0.5 * ((np.sqrt(test_doc_listfr[11]) - np.sqrt(test_doc_listen[1]))**2).sum()))
list1091=[r,s,t,u,v,w]#The textual similarity of the entity 1091 with candidate instances
#Although test_doc_listen[1] is not candidate, i tried test_doc_listfr[11] by using the cross-lingual wikipedia link
