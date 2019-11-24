import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import RegexpTokenizer
from nltk.corpus import brown

from sklearn.decomposition import PCA

from matplotlib import pyplot

element = "main_characters"

filepath = "../data/elements/" + element + ".txt"
filetosave = "../data/elements/" + element + "_dictionary.txt"

def clean_list():
    file = open(filepath, 'rb')
    savefile = open(filetosave, 'w')

    for line in file.readlines():
        words = line.decode('ascii').lower().replace('\'', "").replace(" ", "_").replace("-", "_")
        savefile.write(words)

    file.close()
    savefile.close()

def create_dictionary():
    file = open(filepath, 'r')
    savefile = open(filetosave, 'w')

    for line in file.readlines():
        words = line.lower().replace('\'', "").replace(" ", "_").replace("-", "_")
        savefile.write(line.lower().replace('\'', "").replace('\n', '') + " : " + words)

    file.close()
    savefile.close()

create_dictionary()