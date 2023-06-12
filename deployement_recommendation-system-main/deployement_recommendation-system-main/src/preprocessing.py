
#Package Imported
from nltk.tokenize import word_tokenize
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
import string
import nltk
import os


#run this only first time it will download the packages. It does not need to be run again. It will download the files again from PyPi and it will slow down the execution time
#nltk.download("stopwords")
#nltk.download( 'punkt')






#Class for sanitisation of the text

class sanitisationtext:





    def __init__(self):



        self.regular_punct = list(string.punctuation)

        self.extra_punct = [
                           ',', '.', '"', ':', ')', '(', '!', '?', '|', ';', "'", '$', '&',
                           '/', '[', ']', '>', '%', '=', '#', '*', '+', '\\', '•',  '~', '@', '£',
                           '·', '_', '{', '}', '©', '^', '®', '`',  '<', '→', '°', '€', '™', '›',
                           '♥', '←', '×', '§', '″', '′', 'Â', '█', '½', 'à', '…', '“', '★', '”',
                           '–', '●', 'â', '►', '−', '¢', '²', '¬', '░', '¶', '↑', '±', '¿', '▾',
                           '═', '¦', '║', '―', '¥', '▓', '—', '‹', '─', '▒', '：', '¼', '⊕', '▼',
                           '▪', '†', '■', '’', '▀', '¨', '▄', '♫', '☆', 'é', '¯', '♦', '¤', '▲',
                           'è', '¸', '¾', 'Ã', '⋅', '‘', '∞', '∙', '）', '↓', '、', '│', '（', '»',
                           '，', '♪', '╩', '╚', '³', '・', '╦', '╣', '╔', '╗', '▬', '❤', 'ï', 'Ø',
                           '¹', '≤', '‡', '√', '«', '»', '´', 'º', '¾', '¡', '§', '£', '₤','⌨','☝']

        self.all_punct = list(set(self.regular_punct + self.extra_punct))

        self.stop_words = set(stopwords.words('english'))

        self.file_path_embedding='/home/happyman/Desktop/Projects]/deployement_recommendation-system/models/glove.6B/glove.6B.300d.txt'


    def remove_punctuation(self,text):

        text_str=str(text)

        for punc in self.all_punct:
            if punc in text_str:
                text_str = text_str.replace(punc, ' ')
        return (text_str.strip().lower())


    def tokenise_Sentence(self,data):

        return(word_tokenize(data))


    def remove_spaces(self,text):
        sentenced=[]

        for i in text:
            if len(i) >1:
                sentenced.append(i)

        return(sentenced)

    def remove_stop_words(self,text):

        filtered_sentence = [w for w in text if not w.lower() in self.stop_words]

        return(filtered_sentence)

    def load_embedding(self):
        print("load_embedding")
        embed_dict={}

        with open(self.file_path_embedding, 'r', encoding='utf-8') as f:

            for line in f:
                values = line.split()
                word = values[0]
                coefs = np.asarray(values[1:], dtype='float32')
                embed_dict[word] = coefs
        print("load_embedding retunr")
        return (embed_dict)


    def word_embedding(self,sentence,embed_dict):

        vect_word=[]


        for words in sentence:
            word_vet=[]
            if len(words) >1:
                try:
                    vec=embed_dict[words][0]
                    vect_word.append(vec)
                except:
                    vect_word.append(0)

        return(vect_word)



    def padding(self,sentence,size=10):

        text_size=len(sentence)
        padded_text=[]

        if text_size < size:
            append_size=size-text_size
            for i in sentence:
                padded_text.append(i)

            for i in range(0,append_size):
                padded_text.append(0)

        return(padded_text)
