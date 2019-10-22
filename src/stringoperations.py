import string
import re

numbersregex = r'\d+'

def tolower(text):
    return text.lower()

def toupper(text):
    return text.upper()

def removenumbers(text):
    return re.sub(numbersregex, '', text)

def removepunctuation(text):
    table = str.maketrans("", "", string.punctuation)
    return text.translate(table)

def removewhitespaces(text):
    return text.strip()