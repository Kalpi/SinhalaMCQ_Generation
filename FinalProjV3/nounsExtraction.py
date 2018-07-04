import nltk, re


subject_list = []
object_list = []


def noun_filter(sent_items):
    if sent_items[0] and not sent_items[0] == '.':
        if sent_items[1] == 'S':
            if sent_items[0] not in subject_list:
                subject_list.append(sent_items[0])
        elif sent_items[1] == 'O':
            if sent_items[0] not in object_list:
                object_list.append(sent_items[0])


class NounExtraction:
    @staticmethod
    def extract_nouns(words_set):
        sent_item = []
        tagged_words = re.split('([ub]|[bj]|[ed]|[nj])', words_set)
        for tagged_word in tagged_words:
            if re.match(r'.*_.*', tagged_word):
                striped = tagged_word.strip()
                sent_item = striped.split('_')
            noun_filter(sent_item)
        '''print("subject")
        print(subject_list)
        print("objects")
        print(object_list)'''
        return subject_list


noun_extraction = NounExtraction()
