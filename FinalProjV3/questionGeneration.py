import random, sys
import re
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QListWidget, QListWidgetItem, QLabel, QPushButton, QTextEdit
from PyQt5.QtCore import pyqtSlot
from random import randint
from choiceGeneration import generateChoices
from distractorGeneration import generateDistractors
from questionPhrases import *

last_true_choice = "ඉහත සියල්ල නිවැරදියි"
last_null_choice = "ඉහත කිසිවක් නොවේ"
last_wrong_choice = "ඉහත සියල්ල වැරදියි"
mc_questions = []


def select_choices(keyword, question_type):
    if question_type == 1:
        sentences = generateChoices.search_by_concept(keyword, 4)
        generate_type_one(keyword, sentences)
    elif question_type == 2:
        choices = generateChoices.search_by_concept(keyword, 5)
        generate_type_two(keyword, choices)
    elif question_type == 3:
        choices = generateChoices.search_by_concept(keyword, 4)
        generate_type_three(keyword, choices)
    elif question_type == 4:
        choices = generateDistractors.generate_distractors(keyword, 4)
        print(choices)
        generate_type_four(keyword, choices)
    elif question_type == 5:
        generate_type_five(keyword)


def generate_type_one(keyword, sentences):
    property_list = []
    if sentences:
        for sentence in sentences:
            prop = sentence['predicate']
            if prop not in property_list:
                property_list.append(prop)
                true_choice = sentence['object']
                question = create_type_one_two_question_phrase(1, keyword, prop)
                distractors = generateDistractors.generate_distractors(true_choice, 1)
                if len(distractors) >= 3:
                    true_choice_num = randint(1, 4)
                    # print(true_choice_num)
                    distractor_list = random.sample(distractors, 4)
                    # print(distractor_list)
                    q_generation.text.insertPlainText(question + '\n')
                    # print(question)
                    for num in range(1, 5):
                        if num == true_choice_num:
                            q_generation.text.insertPlainText(' ' + true_choice + '   (T)\n')
                            # print(' ' + true_choice + '   (T)\n')
                        else:
                            q_generation.text.insertPlainText(' ' + distractor_list[num - 1] + '\n')
                            # print(' ' + distractor_list[num - 1] + '\n')
                    q_generation.text.insertPlainText("------------------------------------------------\n")
                    # print("------------------------------------------------")
    # select_choices(keyword, 2)


def create_type_one_two_question_phrase(question_type, keyword, prop):
    if re.match(r'.*ය$', keyword):
        keyword = keyword.replace('ය', 'යේ')

    if question_type == 1:
        if re.match(r'.*දේ$', prop):
            prop = prop.replace('දේ', 'දෙන්නේ')
        elif re.match(r'.*වේ$', prop):
            prop = prop.replace('වේ', 'වන්නේ')
        elif re.match(r'.*නයයි$', prop):
            prop = prop.replace('නයයි', 'නය වන්නේ')
        elif re.match(r'.*ණයයි$', prop):
            prop = prop.replace('ණයයි', 'ණය වන්නේ')
        elif re.match(r'.*යි$', prop):
            prop = prop.replace('යි', 'න්නේ')
        elif re.match(r'.*නී$', prop):
            prop = prop.replace('නී', 'න්නේ')
        elif re.match(r'.*තී$', prop):
            prop = prop.replace('තී', 'තින්නේ')
        elif re.match(r'.*බේ$', prop):
            prop = prop.replace('බේ', 'බෙන්නේ')
        elif re.match(r'.*ඇත$', prop):
            prop = prop.replace('ඇත', 'ඇත්තේ')
        elif re.match(r'.*කි$', prop):
            prop = prop.replace('කි', 'ක් වන්නේ')
        elif re.match(r'.*ටී$', prop):
            prop = prop.replace('ටී', 'ටින්නේ')
        return keyword + ' ' + prop + ' ' + wh_question_plural
    else:
        return keyword + ' ' + prop + ' ' + random.choice(wh_question_integer)


def generate_type_two(keyword, options):
    if options:
        for option in options:
            true_choice_num = randint(1, 4)
            true_choice = option['value']
            value = 1
            question = create_type_one_two_question_phrase(2, keyword, option['predicate'])
            q_generation.text.insertPlainText(question + '\n')
            # print(question)
            for num in range(1, 5):
                if num == true_choice_num:
                    q_generation.text.insertPlainText(' ' + str(true_choice) + '   (T)\n')
                    # print(' ' + str(true_choice) + '   (T)')
                    continue
                value = value + 1
                if value == true_choice:
                    value = value + 1
                q_generation.text.insertPlainText(' ' + str(value) + '\n')
                # print(' ' + str(value))
            q_generation.text.insertPlainText('------------------------------------------------\n')
        # print("------------------------------------------------")
    select_choices(keyword, randint(3, 4))


def generate_type_three(keyword, choices):
    if choices:
        if len(choices) >= 3:
            choices = random.sample(choices, 3)
            q_generation.text.insertPlainText(keyword + question_type3 + '\n')
            # print(keyword + question_type3)
            for choice in choices:
                q_generation.text.insertPlainText(" " + choice['subject'] + " " + choice['object'] + " " +
                                                  choice['predicate'] + '\n')
                # print(" " + choice['subject'] + " " + choice['object'] + " " + choice['predicate'])
            q_generation.text.insertPlainText(" " + last_true_choice + '   (T)\n')
            # print(" " + last_true_choice + '   (T)')
            q_generation.text.insertPlainText('------------------------------------------------\n')
            # print("------------------------------------------------")
        else:
            distractor_num = 3 - len(choices)
            distractors = create_distractors(keyword, distractor_num, 3)
            if distractors and len(distractors) >= distractor_num:
                distractors = random.sample(distractors, distractor_num)
                q_generation.text.insertPlainText(keyword + question_type3 + '\n')
                # print(keyword + question_type3)
                for choice in choices:
                    q_generation.text.insertPlainText(" " + choice['subject'] + " " + choice['object'] + " " +
                                                      choice['predicate'] + '   (T)\n')
                    # print(" " + choice['subject'] + " " + choice['object'] + " " + choice['predicate'] + '   (T)')
                for distractor in distractors:
                    q_generation.text.insertPlainText(" " + distractor['subject'] + " " + distractor['object'] + " " +
                                                      distractor['predicate'] + '\n')
                    # print(" " + distractor['subject'] + " " + distractor['object'] + " " + distractor['predicate'])
                q_generation.text.insertPlainText(" " + last_true_choice + '\n')
                # print(" " + last_true_choice)
                q_generation.text.insertPlainText('------------------------------------------------\n')
                # print("------------------------------------------------")
            else:
                select_choices(keyword, 1)
    else:
        distractors = create_distractors(keyword, 4, 3)
        if distractors:
            q_generation.text.insertPlainText(keyword + question_type3 + '\n')
            # print(keyword + question_type3)
            for distractor in distractors[0: 3]:
                q_generation.text.insertPlainText(" " + distractor['subject'] + " " + distractor['object'] + " " +
                                                  distractor['predicate'] + '\n')
                # print(" " + distractor['subject'] + " " + distractor['object'] + " " + distractor['predicate'])
            q_generation.text.insertPlainText(' ' + last_null_choice + '   (T)\n')
            # print(" " + last_null_choice + '   (T)')
            q_generation.text.insertPlainText('------------------------------------------------\n')
            # print("------------------------------------------------")


def generate_type_four(keyword, choices):
    print(choices)
    if choices:
        if len(choices) >= 3:
            choices = random.sample(choices, 3)
            q_generation.text.insertPlainText(keyword + question_type4 + '\n')
            # print(keyword + question_type4)
            for choice in choices:
                q_generation.text.insertPlainText(" " + choice['subject'] + " " + choice['object'] + " " +
                                                  choice['predicate'] + '\n')
                # print(" " + choice['subject'] + " " + choice['object'] + " " + choice['predicate'])
            q_generation.text.insertPlainText(' ' + last_wrong_choice + '   (T)\n')
            # print(" " + last_wrong_choice + '   (T)')
            q_generation.text.insertPlainText('------------------------------------------------\n')
            # print("------------------------------------------------")
        else:
            distractor_num = 3 - len(choices)
            distractors = create_distractors(keyword, distractor_num, 4)
            if distractors and len(distractors) >= distractor_num:
                q_generation.text.insertPlainText(keyword + question_type4 + '\n')
                # print(keyword + question_type4)
                for choice in choices:
                    q_generation.text.insertPlainText(" " + choice['subject'] + " " + choice['object'] + " " +
                                                      choice['predicate'] + '   (T)\n')
                    # print(" " + choice['subject'] + " " + choice['object'] + " " + choice['predicate'] + '   (T)')
                for distractor in distractors[0: distractor_num]:
                    q_generation.text.insertPlainText(" " + distractor['subject'] + " " + distractor['object'] + " " +
                                                      distractor['predicate'] + '\n')
                    # print(" " + distractor['subject'] + " " + distractor['object'] + " " + distractor['predicate'])
                q_generation.text.insertPlainText(" " + last_wrong_choice + '\n')
                # print(" " + last_wrong_choice)
                q_generation.text.insertPlainText('------------------------------------------------\n')
                # print("------------------------------------------------")
    else:
        distractors = create_distractors(keyword, 4, 4)
        if distractors:
            q_generation.text.insertPlainText(keyword + question_type4 + '\n')
            # print(keyword + question_type4)
            for distractor in distractors[0: 3]:
                q_generation.text.insertPlainText(" " + distractor['subject'] + " " + distractor['object'] + " " +
                                                  distractor['predicate'] + '\n')
                # print(" " + distractor['subject'] + " " + distractor['object'] + " " + distractor['predicate'])
            q_generation.text.insertPlainText(" " + last_null_choice + '   (T)\n')
            # print(" " + last_null_choice + '   (T)')
            q_generation.text.insertPlainText('------------------------------------------------\n')
            # print("------------------------------------------------")
        else:
            print("No enough content in the ontology")


def generate_type_five(keyword):
    distract_words = []
    keyword_phrases = generateChoices.search_by_concept(keyword, 4)
    print(keyword_phrases)
    if keyword_phrases:
        if len(keyword_phrases) >= 2:
            print('pass 1')
            siblings = generateChoices.search_by_concept(keyword, 3)
            sib_length = len(siblings)
            print(sib_length)
            if sib_length >= 1:
                print('pass 2')
                for sibling in siblings:
                    sib_phrases = generateChoices.search_by_concept(sibling, 4)
                    if len(sib_phrases) >= 2:
                        print('pass 3')
                        if sib_length == 1:
                            print('get parent')
                            distract_words = generateChoices.search_by_concept(keyword, 1)
                        else:
                            print('get siblings')
                            for sib in siblings:
                                if not sib == sibling:
                                    distract_words.append(sib)
                        q_generation.text.insertPlainText('පහත සඳහන් අවස්ථා සලකන්න.\n අවස්ථාව 1:\n')
                        print('පහත සඳහන් අවස්ථා සලකන්න.\n අවස්ථාව 1:')
                        for key_phrase in random.sample(keyword_phrases, 2):
                            q_generation.text.insertPlainText("  X " + key_phrase['object'] + ' ' + key_phrase['predicate'] + '\n')
                            print("  X " + key_phrase['object'] + ' ' + key_phrase['predicate'])
                        q_generation.text.insertPlainText(' අවස්ථාව 2:\n')
                        print(' අවස්ථාව 2:')
                        for sib_phrase in random.sample(sib_phrases, 2):
                            q_generation.text.insertPlainText("  Y " + sib_phrase['object'] + ' ' + sib_phrase['predicate'] + '\n')
                            print("  Y " + sib_phrase['object'] + ' ' + sib_phrase['predicate'])
                        q_generation.text.insertPlainText('X සහ Y හඳුනාගන්න.\n')
                        print('X සහ Y හඳුනාගන්න.')
                        distract = random.sample(distract_words, 1)
                        print("distract " + distract[0])
                        choices = [keyword + ', ' + sibling + '   (T)', sibling + ', ' + keyword,
                                   keyword + ', ' + distract[0], distract[0] + ', ' + keyword]
                        for choice in random.sample(choices, 4):
                            q_generation.text.insertPlainText(' ' + choice + '\n')
                            print(' ' + choice)
                        q_generation.text.insertPlainText('------------------------------------------------\n')
                    else:
                        continue
            else:
                select_choices(keyword_phrases, 4)
    else:
        q_generation.text.insertPlainText('කරුණු ප්‍රමාණවත් නොවේ')
        print("no phrases")


def create_distractors(concept, distractor_num, question_type):
    distractors = []
    if question_type == 3:
        distractors = generateDistractors.generate_distractors(concept, 4)
    elif question_type == 4:
        distractors = generateChoices.search_by_concept(concept, 4)
    if len(distractors) >= distractor_num:
        return distractors


class QuestionsGeneration(QWidget):
    def __init__(self):
        super(QuestionsGeneration, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(600, 850)
        self.move(610, 0)
        self.setWindowTitle('බහුවරණ ප්‍රශ්නාවලිය')

        self.text = QTextEdit(self)
        self.text.resize(600, 810)

        self.show()

    @staticmethod
    def generate_questions(keywords, q_type):
        q_generation.text.clear()
        '''keywords = ['වර්ණදේහ', 'ෙසෙල', 'ෙසෙල වාදය', 'ඌනන විභාජනය', 'අනූනන විභාජනය', 'අන්තඃප්ලාස්මීය ජාලිකා',
                    'රළු අන්තඃප්ලාස්මීය ජාලිකා', 'සිනිඳු අන්තඃප්ලාස්මීය ජාලිකා', 'න්‍යෂ්ටිකාව', 'චර්ම ෙසෙල',
                    'ප්ලාස්ම පටලය']
        print(len(keywords))'''
        for keyword in keywords:
            if q_type == 1:
                question_type = 1
            elif q_type == 2:
                question_type = 2
            elif q_type == 3:
                question_type = 3
            elif q_type == 4:
                question_type = 4
            elif q_type == 5:
                question_type = 5
            elif q_type == 6:
                question_type = randint(1, 4)
            print(keyword + " " + str(question_type))
            select_choices(keyword, question_type)


ex = QApplication([])
q_generation = QuestionsGeneration()


