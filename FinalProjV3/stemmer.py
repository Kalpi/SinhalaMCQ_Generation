import sys
import re
from nltk import word_tokenize
from vocabulary import *


def identify_subject(stemmed_words):
    word_phrase = ''
    tagging_word = ''
    tagged_subject_set = []
    for word in stemmed_words:
        word_phrase = word_phrase + word + ' '
        if word_phrase in vocabulary:
            tagging_word = word_phrase.rstrip()
            tagged_subject_set.clear()
            tagged_subject_set.append(tagging_word + '_Sub')
    subject = tagged_subject_set[0]
    obj = identify_object(word_phrase, tagging_word)
    object_word = obj.replace('_Obj', '')
    verb_phrase = word_phrase.replace(tagging_word, '').replace(object_word, '').strip() + '_Pred'
    return subject + ' ' + obj + ' ' + verb_phrase + ' '


def identify_object(word_phrase, tagged_subject):
    phrase = ''
    tagged_object_set = []
    sent_wo_subject = word_phrase.replace(tagged_subject, '').lstrip()
    words_wo_subject = word_tokenize(sent_wo_subject)
    for word in words_wo_subject:
        phrase = phrase + word + ' '
        if phrase in vocabulary:
            tagging_word = phrase.rstrip()
            tagged_object_set.clear()
            tagged_object_set.append(tagging_word + '_Obj')
    return tagged_object_set[0]


class WordsStem:
    @staticmethod
    def stemming_words(words):
        stemmed_words = []
        stemmed_phrase = ''
        for word in words:
            if word not in verb_phrase_words:
                if re.match(r'^.*වල$', word):
                    word = word.replace('වල', '')
                elif re.match(r'^.*වක්$', word):
                    word = word.replace('වක්', '')
                elif re.match(r'^.*වලින්$', word):
                    word = word.replace('වලින්', '')
                elif re.match(r'^.*වට$', word):
                    word = word.replace('වට', '')
                elif re.match(r'^.*යට$', word):
                    word = word.replace('යට', '')
                elif re.match(r'^.*වලට$', word):
                    word = word.replace('වලට', '')
                elif re.match(r'^.*කින්$', word):
                    word = word.replace('කින්', '')
                elif re.match(r'^.*ක්$', word):
                    word = word.replace('ක්', '')
                elif re.match(r'^.*ට$', word):
                    word = word.replace('ට', '')
                elif re.match(r'^.*යෙන්$', word):
                    word = word.replace('යෙන්', 'ය')
                elif re.match(r'^.*යේදී$', word):
                    word = word.replace('යේදී', 'ය')
                elif re.match(r'^.*ෙසෙලයේ$', word):
                    word = word.replace('ෙසෙලයේ', 'ෙසෙල')
                elif re.match(r'^.*යේ$', word):
                    word = word.replace('යේ', 'ය')
                elif re.match(r'^.*ර්ණයේ$', word):
                    word = word.replace('ර්ණයේ', 'ර්ණ')
            if not word == '.':
                stemmed_words.append(word)
                stemmed_phrase = stemmed_phrase + word + ' '
        tagged_phrase = identify_subject(stemmed_words)
        return tagged_phrase


words_stemming = WordsStem()
# words_stemming.stemming_words(['ෙසෙල', 'විභාජනයේදී', 'වෙනස්කම්', 'සිදු', 'වේ', '.'])
