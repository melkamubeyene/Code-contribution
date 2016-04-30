import codecs
import wikipedia
import os
wikipedia.set_lang("fr")
os.chdir='/home/sciencelib/Desktop/Melkamu_Data/test_data/testfrenchwiki'
English_Titles=open('/home/sciencelib/Desktop/Melkamu_Data/test_data/fr')
for items in English_Titles.readlines():
        document_collection=codecs.open(items,'w', encoding='utf8')
        document_collection.write(wikipedia.summary(items))
        document_collection.close()

