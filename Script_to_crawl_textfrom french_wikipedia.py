import codecs
import wikipedia
wikipedia.set_lang("fr")
English_Titles=open('/home/melkamu/  /Documents_for_testing/french_Resource')
document_collection=codecs.open('/home/melkamu/  /Documents_for_testing/French_wikipedia','w', encoding='utf8')
for items in English_Titles.readlines():
    document_collection.write('\n<doc_sep>\n')
    #document_collection.write(items)
    document_collection.write(wikipedia.summary(items))
