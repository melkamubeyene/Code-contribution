# -*- coding: utf-8 -*-
import rdflib
import scipy as sc
import pandas as pd
import matplotlib.pyplot as plt
import scipy.sparse
import sklearn
from sktensor import dtensor, cp_als
from sktensor import rescal
from sktensor import ktensor
from sktensor import sptensor
from sktensor import dtensor
from sklearn.metrics.pairwise import cosine_similarity
from sktensor import cp
import numpy as np
import codecs
from rdflib import Graph, RDF, URIRef, Literal
g=Graph()
g.parse('/home/melkamu/  /Documents_for_testing/English_Test_Dataset_Final', format='nt')#the english DBpedia graph
g.parse('/home/melkamu/  /Documents_for_testing/French_Test_Dataset_Final', format='nt')#the french DBpedia graph
Subject_object_tuple={}
for x,y in g.subject_objects(predicate=None):
        if (x,y):
                Subject_object_tuple[x,y]=1
keys=np.array(Subject_object_tuple.keys())
vals=np.array(Subject_object_tuple.values())
unq_keys, key_idx = np.unique(keys, return_inverse=True)
key_idx_ = key_idx.reshape(-1,2)
n = len(unq_keys)
Subject_mat =scipy.sparse.lil_matrix((n, n) ,dtype=float)
dictionary={}
dictionary2={}
dictionary3={}
def predicate(predicate):
        Subject_slice={}
        for x,y in predicate:
                if (x,y):
                        Subject_slice[x,y]=1
        keys1=np.array(Subject_slice.keys())
        vals1=np.array(Subject_slice.values())
        unq_keys1, key_idx1 = np.unique(keys1, return_inverse=True)
        for i in range(len(unq_keys)):
                dictionary[unq_keys[i]]=i
        for i in range(len(unq_keys1)):
                dictionary2[unq_keys1[i]]=i
        liv=dictionary2.values();
        for i in dictionary2.keys():
                if i in dictionary.keys():
                        dictionary2[i]=dictionary[i]
        dictionary3=dict(zip(liv,dictionary2.values()))
        for y in range(len(key_idx1)):
                key_idx1[y]=dictionary3[key_idx1[y]]
        key_idx_1 = key_idx1.reshape(-1,2)
        Subject_mat[key_idx_1[: ,0], key_idx_1[: ,1]]= 1
        return Subject_mat                              
RDF_Type=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://www.w3.org/1999/02/22-rdf-syntax-ns#type')))
OWL_SameAs=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://www.w3.org/2002/07/owl#sameAs')))
Subject=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://purl.org/dc/terms/subject')))
Influence=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/influences')))
BirthPlace=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/birthPlace')))
Occupation=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/occupation')))
wikiPageExternalLink=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/wikiPageExternalLink')))
Country=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/country')))
profesion=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/profession')))
nationality=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/nationality')))
deathplace=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/deathPlace')))
title=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/title')))
formerteam=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/formerTeam')))
league=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/league')))
position=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/position')))
team=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/team')))
termperiod=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/termPeriod')))
website=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/website')))
careerstation=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/careerStation')))
clubs=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/clubs')))
currentclub=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/currentclub')))
nationalteam=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/nationalteam')))
youth=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/youthclubs')))
Chancellor=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/chancellor')))
party=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/party')))
religion=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/religion')))
spouse=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/spouse')))
sucees=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/successor')))
battle=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/battle')))
militaryrank=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/militaryBranch')))
relation=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/relation')))
branch=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/branch')))
rank=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/rank')))
first=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/firstRace')))
last=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/lastRace')))
strokes=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/strokes')))
collegeteam=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/collegeteam')))
associatedband=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/associatedBand')))
associatedmusic=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/associatedMusicalArtist')))
genre=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/genre')))
hometown=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/hometown')))
recordlev=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/recordLabel')))
origion=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/origin')))
word_net=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/wordnet_type')))
after=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/after')))
before=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/before')))
predecessor=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/predecessor')))
successor=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/successor')))
language=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/languagesSpoken')))
residence=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/residence')))
parent=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/parent')))
father=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/father')))
house=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/house')))
issue=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/issue')))
mother=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/mother')))
coach=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/coach')))
instrument=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/instrument')))
label=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/label')))
alongside=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/alongside')))
consitency=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/constituencyMp')))
deputy=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/deputy')))
govegene=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/governorGeneral')))
honpref=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/honorificPrefix')))
monarch=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/monarch')))
office=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/office')))
order=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/order')))
prime=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/property/primeminister')))
movie=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/movie')))
education_place=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/educationPlace')))
decoration=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/decoration')))
decipline=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/disciple')))
education=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/education')))
mentor=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/mentor')))
university=predicate(g.subject_objects(predicate=rdflib.term.URIRef(u'http://dbpedia.org/ontology/university')))
#Tensor Factorization by ALS
A, R,_, _, _ = rescal.als([0.0001*RDF_Type,0.0001*Subject,OWL_SameAs,Influence,BirthPlace,Occupation,wikiPageExternalLink,Country,profesion,nationality,deathplace,title,formerteam,league,position,team,termperiod,website,careerstation,clubs,currentclub,nationalteam,youth,Chancellor,party,religion,spouse,sucees,battle,militaryrank,relation,branch,rank,first,last,strokes,collegeteam,associatedband,associatedmusic,genre,hometown,recordlev,origion,word_net,after,before,predecessor,successor,language,residence,parent,father,house,issue,mother,coach,instrument,label,alongside,consitency,deputy,govegene,honpref,monarch,office,order,prime,movie,education_place,decoration,decipline,education,mentor,university],100)
simstru=cosine_similarity(A, A)#applying cosine similarity
pd=pd.DataFrame(simstru)#A data structure to identify the location of resources in memory
pd2=pd.copy()
