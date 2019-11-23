import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import RegexpTokenizer
from nltk.corpus import brown

import gensim

from sklearn.decomposition import PCA

from matplotlib import pyplot

filepath = "../data/main_characters.txt"
filetosave = "../data/main_characters_processed.txt"

file = open(filepath, 'rb')
savefile = open(filetosave, 'w')

for line in file.readlines():
    words = line.decode('ascii').lower().replace('\'', "").replace(" ", "_").replace("-", "_")
    savefile.write(words)

file.close()
savefile.close()