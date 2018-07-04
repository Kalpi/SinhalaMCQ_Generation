import sys
import nltk
import re
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextEdit
from PyQt5.QtCore import pyqtSlot
from nltk import word_tokenize, sent_tokenize
from stemmer import words_stemming
from nounsExtraction import noun_extraction
from questionGeneration import q_generation

stemmed_sentences = []


def split_sentences(full_text):
    splited_sentences = sent_tokenize(full_text)
    return splited_sentences


def split_words(full_text):
    splited_words = []
    splited_text = re.split('\n\n| \n|\n|[ ]|,', full_text)
    for word in splited_text:
        if not word == '':
            splited_words.append(word)
    return splited_words


def remove_stopwords(full_text, stopwords_list):
    summed_phrase = ''
    words = split_words(full_text)
    for word in words:
        if word not in stopwords_list:
            summed_phrase = summed_phrase + word + ' '
    return summed_phrase


def stemming_sentence(sentence_wo_stopwords):
    sentence_words = word_tokenize(sentence_wo_stopwords)
    stemmed_sentence = words_stemming.stemming_words(sentence_words)
    return stemmed_sentence


def summarize_text(full_text, stopwords_list):
    summed_text = ''
    text_wo_stopwords = remove_stopwords(full_text, stopwords_list)
    sentences = sent_tokenize(text_wo_stopwords)
    for sentence in sentences:
        stemmed_sentence = stemming_sentence(sentence)
        # print(stemmed_sentence)
        summed_text = summed_text + stemmed_sentence
    return summed_text


def get_stopwords(stopwords):
    stopwords_new = []
    stopwords_list = nltk.word_tokenize(stopwords)
    for word in stopwords_list:
        if not word.isdigit():
            stopwords_new.append(word)
    return stopwords_new


class PreProcessing:
    @staticmethod
    def start(full_text):
        stopwords = open('StopWords_sin.txt', 'r', encoding='utf-16').read()
        stopwords_list = get_stopwords(stopwords)
        '''full_text = "රයිබොසෝම ඉන්ද්‍රයිකා වර්ගයකි. රයිබොසෝම ෙසෙල ප්ලාස්මයේ නිදහස්ව පවතී. " \
                    "රයිබොසෝම රළු අන්තඃප්ලාස්මීය ජාලිකා වලට සම්බන්ධව පවතී."'''
        summarized_text = summarize_text(full_text, stopwords_list)
        keywords = noun_extraction.extract_nouns(summarized_text)
        # q_generation.generate_questions(keywords)
        return keywords


text_pre_process = PreProcessing()
