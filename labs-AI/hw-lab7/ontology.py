"""
http://profs.info.uaic.ro/~ipistol/ia1617/index.php?showpage=0206

"""
'''
from SPARQLWrapper import SPARQLWrapper, JSON, XML, N3, RDF

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?label
    WHERE { <http://dbpedia.org/resource/Asturias> rdfs:label ?label }
""")
'''

"""
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX foaf: <http://xmlns.com/foaf/0.1/>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX quepy: <http://www.machinalis.com/quepy#>
            PREFIX dbpedia: <http://dbpedia.org/ontology/>
            PREFIX dbpprop: <http://dbpedia.org/property/>
            PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
            
            SELECT DISTINCT ?label WHERE {
              ?x0 rdfs:label "==@en.
              ?x0 rdfs:label ?label.
            filter langMatches(lang(?label),"en")
"""
"""
 PREFIX dbpedia: <http://dbpedia.org/ontology/>
 PREFIX dbres: <http://dbpedia.org/resource/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            
            SELECT DISTINCT ?type WHERE {
              dbres:Italy rdf:type ?type
            }
"""

#https://github.com/smilli/py-corenlp
from nltk.tokenize import TweetTokenizer
from nltk.stem import WordNetLemmatizer

from pycorenlp import StanfordCoreNLP



from SPARQLWrapper import SPARQLWrapper, JSON

import sys
import codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)


file_text = open("source.txt", 'r').read()

#nltk.download
#if wordnet corpus not present

def nltk_tokenize(text):
    tokens = []

    tknzr = TweetTokenizer()
    tokens = tknzr.tokenize(text)

    return tokens

def nltk_lemmatize(tokens):
    wnl = WordNetLemmatizer()
    for i in range(len(tokens)):
        tokens[i] = wnl.lemmatize(tokens[i])
    return tokens

def corenlp_tokenize(text):
    nlp = StanfordCoreNLP('http://localhost:9000')
    output = nlp.annotate(text, properties={
        'annotators': 'tokenize,ssplit,pos,depparse,parse',
        'outputFormat': 'json'
    })
    print(output['sentences'][0]['parse'])

    return output

def sparql_query(tokens):
    sparql = SPARQLWrapper("https://dbpedia.org/sparql")
                    # http nope, https strange characters
    tokens_labels = {}

    for item in tokens:
        print item
        sparql.setQuery("""
            PREFIX dbpedia: <http://dbpedia.org/ontology/>
            PREFIX dbres: <http://dbpedia.org/resources/>
            
            SELECT DISTINCT ?type WHERE {
              dbres:Italy rdfs:type ?type
            }
        """)

        print '\n\n*** JSON:\n'
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

        for result in results["results"]["bindings"]:
            print(result["label"]["value"])
        break


tokens = nltk_tokenize(file_text)
print 'tokenized: ', tokens

tokens = nltk_lemmatize(tokens)
print 'lemmatized', tokens

sparql_query(tokens)

