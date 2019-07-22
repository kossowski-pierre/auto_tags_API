import pandas as pd
import numpy as np

import nltk
#from bs4 import BeautifulSoup
from nltk.tokenize.simple import SpaceTokenizer

from sklearn.naive_bayes import BernoulliNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics


import pickle
with open('./AutoTagAPP/model_supervise.obj', 'rb') as f:
	model_b, tfidf = pickle.load(f)
with open('./AutoTagAPP/etiquettesTags.pkl', 'rb') as y:
	etiqu_tags=pickle.load(y)	

def tokenize(text):
    """le pattern pour tokenizer"""
    tmp = nltk.tokenize.RegexpTokenizer(r'[a-zA-Z#+\.]+\-?[a-zA-Z#+]+|\b[crCR]\b').tokenize(text) 
    return tmp

stop = nltk.corpus.stopwords.words('english')
wnet = nltk.WordNetLemmatizer()


def text_transform(text):
	#wnet.ensure_loaded() 
    text_l=tokenize(text)
    text_l=[wnet.lemmatize(w) for w in text_l if w not in stop]
    text_l=[w.lower() for w in text_l]
    return tfidf.transform([' '.join(text_l)])

def tags_5(pred):
    """retourne les 5 tags les plus probables"""
    l_pred = []
    for ind in np.argsort(pred)[:-5:-1]:
        l_pred.append(etiqu_tags[ind])
    return l_pred

def get_tags(text):
	text_vect=text_transform(text).todense()
	
	pred = pd.Series(range(len(etiqu_tags))).apply(lambda x: model_b.loc['model', x].predict_proba(text_vect)[:,1])
	return tags_5(pred)


