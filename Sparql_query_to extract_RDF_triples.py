import rdflib
from rdflib import Graph, URIRef, Namespace
from SPARQLWrapper import SPARQLWrapper, JSON, RDF,N3
sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
      PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
      PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
      PREFIX foaf: <http://xmlns.com/foaf/0.1/>
      PREFIX xml: <http://www.w3.org/XML/1998/namespace>
      PREFIX owl: <http://www.w3.org/2002/07/owl#>
      PREFIX dbpedia: <http://www.dbpedia.org.resources>
      PREFIX dbpediaonto: <http://www.dbpedia.org/ontology>
      PREFIX dbpediafr: <http://fr.dbpedia.org/ontology>
      PREFIX dbpedia_french: <http://fr.dbpedia.org>
      PREFIX sub: <http://purl.org/dc/terms>
select ?s ?p ?o1
where {?s a <http://dbpedia.org/ontology/Institution> .
        ?s owl:sameAs ?o .
        ?s ?p ?o1 .
filter(strstarts(str(?o),"http://fr.dbpedia.org"))
filter(strstarts(str(?o2),"http://fr.dbpedia.org")) 
FILTER(isIRI(?o1))
FILTER(isIRI(?s))
}  """)
sparql.setReturnFormat(turtle)
results = sparql.query().convert()

