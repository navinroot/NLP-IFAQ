#!/usr/bin/env python

import nltk, re, pprint
import sys
import re
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
import itertools
from nltk.corpus import wordnet as wn
################### read corpus file
fo = open("output/corpus.txt", "r+")
html= fo.read();
fo.closed

 ###################function to check synonyms
def Synonym_Checker(word1, word2):
    """Checks if word1 and word2 and synonyms. Returns True if they are, otherwise False"""
    if word1.lower()==word2.lower():
		match=True
    else:
	    equivalence = WordNetLemmatizer()
	    word1 = equivalence.lemmatize(word1)
	    word2 = equivalence.lemmatize(word2)
	 	
	    word1_synonyms = wordnet.synsets(word1)
	    word2_synonyms = wordnet.synsets(word2)
	 
	    scores = [i.wup_similarity(j) for i, j in list(itertools.product(word1_synonyms, word2_synonyms))]
	    if len(scores)!=0:
		    max_index = scores.index(max(scores))
		    best_match = (max_index/len(word1_synonyms), max_index % len(word1_synonyms)-1)
		    try:
		    	word1_set = word1_synonyms[best_match[1]].lemma_names
		    except:
		    	word1_set = word1_synonyms[best_match[0]].lemma_names
		    try:
		    	word2_set = word2_synonyms[best_match[1]].lemma_names
		    except:
		    	word2_set = word2_synonyms[best_match[0]].lemma_names
		    match = False
		    match = [match or word in word2_set for word in word1_set][0]
	    else:
	 		match=False
    if match==True:
    	return match
    else:
	    word2_synonyms = wordnet.synsets(word1)
	    word1_synonyms = wordnet.synsets(word2)
	 
	    scores = [i.wup_similarity(j) for i, j in list(itertools.product(word1_synonyms, word2_synonyms))]
	    if len(scores)!=0:
		    max_index = scores.index(max(scores))
		    best_match = (max_index/len(word1_synonyms), max_index % len(word1_synonyms)-1)
		    try:
		    	word1_set = word1_synonyms[best_match[1]].lemma_names
		    except:
		    	word1_set = word1_synonyms[best_match[0]].lemma_names
		    try:
		    	word2_set = word2_synonyms[best_match[1]].lemma_names
		    except:
		    	word2_set = word2_synonyms[best_match[0]].lemma_names
		    match = False
		    match = [match or word in word2_set for word in word1_set][0]
	    else:
	 		match=False
    return match
###################################################################
###################function to find synonyms
def synonyms(s):
	l=wn.synsets(s)
	if len(l)==0:
		return 0
	else:
		return 1
##########################################query important word extraction
from nltk.tag import pos_tag
sentence = str(sys.argv[1])
tagged_sent = pos_tag(sentence.split())
#print tagged_sent
imp_query = [word for word,pos in tagged_sent if pos == 'NN' or pos == 'NNP' or pos == 'JJ' or pos == "VBG" or pos == "VBD" or pos == "VBP" or pos=="VB" or pos=="VBN" or pos == 'JJR' or pos == 'JJS' or pos == 'NNS' or pos == "NNPS" or pos == "RB" or pos == "RBR" or pos=="RBS"]
#print imp_query
noun=[]
for i in xrange(0,len(imp_query)):
	if synonyms(imp_query[i])==0:
		noun.append(imp_query[i])
		if len(noun)==3:
			i=len(imp_query)+2


try:
	imp_query.remove("was")
	imp_query.remove("were")
	imp_query.remove("will")
	imp_query.remove("can")
	imp_query.remove("could")
	imp_query.remove("would")
except Exception, e:
	flag=0
	

#print len(noun)
#print imp_query
##########################################file handling
flag=0
try:
    with open('ans/data.txt',"r") as fh:
    	content=fh.read()
	if len(content)!=0:
		data=int(content)+1
		data=data%12
		if data==0:
			data=2
    	    	flag=1
except IOError:
	fh=open('ans/data.txt',"w")
	data=2
	fh.write(str(data))
	fh.close()
fh.close()
if flag==1:
	fh=open('ans/data.txt',"w")
	fh.write(str(data))
	fh.close()

#print data
##########################################working on corpus
htm=nltk.sent_tokenize(html)
#print htm[0]
#print len(htm)
strr=""
data=data-1
#print noun
if len(noun)>0:
	for x in xrange(0,len(htm)):
		if any(i in htm[x] for i in noun):
			strr=strr+" "+htm[x]
else:
	strr=html
	
st=nltk.sent_tokenize(strr)
stri=nltk.sent_tokenize(strr)
#print st[0]
#print len(st)

###################################marking approximation
arr=[]
#print noun
#print imp_query
for x in range(len(st)):
	flag=0
	st[x]=st[x].translate(None,".")
	st[x]=st[x].translate(None,",")
	words = st[x].split()
	st[x] =" ".join(sorted(set(words), key=words.index))
	tagged_c = pos_tag(st[x].split())
	imp_d = [word for word,pos in tagged_c if pos == 'NN' or pos == 'NNP' or pos == "VBG" or pos == 'JJ' or pos == "VBD" or pos == "VBP" or pos=="VB" or pos=="VBN" or pos == 'JJR' or pos == 'JJS' or pos == 'NNS' or pos == "NNPS" or pos == "RB" or pos == "RBR" or pos=="RBS"]
	for y in range(len(imp_query)):
		for z in range(len(imp_d)):
			if Synonym_Checker(imp_query[y],imp_d[z])==True:
				flag=flag+1
				break
	arr.append(flag)
#print arr
f=open("ans/"+str(data)+".txt","w")
if len(st)>=5:
	for i in xrange(5):
		ind=arr.index(max(arr))
		arr[ind]=-1
		f.write(stri[ind]+"\n")
else:
	for i in xrange(len(st)):
		ind=arr.index(max(arr))
		arr[ind]=-1
		f.write(stri[ind]+"\n")
f.close()
print data	
#print arr	
