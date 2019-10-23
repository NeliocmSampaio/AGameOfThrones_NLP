# -*- coding: utf-8 -*-
"""Got1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u51-aEwMICoF2FnS8gD1yqfDjstgNZtd
"""

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import RegexpTokenizer
from nltk.corpus import brown

import gensim

forgooglecolab = True
if forgooglecolab:
  from google.colab import files
  uploaded = files.upload()

if forgooglecolab:
  filepath = "got1.txt"
else:
  filepath = "../data/got1.txt"

file = open(filepath)
lines = file.readlines()

for index, line in enumerate(lines):
  if "PROLOGUE" in line:
    lines = lines[index+1:]

sentences = []
for line in lines:
  if len(line) > 1:
    for sentence in sent_tokenize(line):
      sentences.append(sentence)

#print(sentences)

stop_words = set(stopwords.words("english"))
tokenizer = RegexpTokenizer(r'\w+')
filtered_sentences = []

for sentence in sentences:
  sent = []
  strspace = " "
  #print(sent.join(tokenizer.tokenize(str(sentence))))
  for word in word_tokenize( " ".join(tokenizer.tokenize(str(sentence)))):
    if word not in list(stop_words):
      sent.append(word.lower())
  filtered_sentences.append(" ".join(sent))

#print(filtered_sentences[:100])

model = gensim.models.Word2Vec(filtered_sentences)

model.vocabulary