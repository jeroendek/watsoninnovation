import json
import os
import sys
from watson_developer_cloud import NaturalLanguageClassifierV1
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import neural_network
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import r2_score
import pandas as pd

natural_language_classifier = NaturalLanguageClassifierV1(
    username='b2ca77b4-8191-4b56-b542-8b2e716e0bd8',
    password='C2q0t1AhFRbh'
)
print("Initializing the application, please wait a few seconds.")
skill_data = pd.read_csv(os.getcwd()+'/Data/dataset_nn.csv', header=0
                        ,  names=["education", "age", "interest", "num_of_questions", "perc_correct", "avg_time_to_answer", "prev_skill_level", "feedback", "pred_skill_level"])

X = skill_data.drop('pred_skill_level', axis=1)
y = skill_data['pred_skill_level']

mlp = MLPRegressor(hidden_layer_sizes=(20,13,13,20),max_iter=500)
mlp.fit(X, y)

class Student:

    def __init__(self,name):
        self.name = name
        self.level = 0
        self.score = 0
        self.interests = []
        self.num_answered = 0
        self.num_correct = 0
        self.interest_level = 0
        self.education = 0
        self.question_path = []
        self.feedback_path = []
        self.answer_path = []

    def alter_level(self,level):
        self.level = level

    def add_interest(self, interests):
        self.interests = interests

    def add_interest_level(self, interest_level):
        self.interest_level = interest_level

    def set_question_path(self,question_path):
        self.question_path = question_path

    def set_study(self,education):
        self.education = education

    def add_score(self,points):
        self.score += points

    def add_feedback(self,feedback):
        self.feedback_path.append(feedback)

    def add_answer(self,correctness):
        self.answer_path.append(correctness)

class Question:

    def __init__(self, name):
        self.name = name
        self.answers = []
        self.category = 'unknown'

    def alter_category(self, category):
        self.category = category

    def add_answer(self, answer):
        self.answers.append(answer)

    def replace_answer(self,answer_old,answer_new):
        [s.replace(answer_old,answer_new) for s in self.answers]

class Answer:

    def __init__(self,name):
        self.name = name
        self.level = 0
        self.is_true = False

    def alter_level(self,level):
        self.level = level

    def set_true(self, boolean):
        self.is_true = boolean


Q1 = Question('Where did the Anatomy Lesson take place?')
Q1.add_answer(Answer('Amsterdam'))
Q1.answers[0].set_true(True)
Q1.add_answer(Answer('Zaandam'))
Q1.add_answer(Answer('Den Haag'))
Q1.add_answer(Answer('Haarlem'))
Q1.add_answer(Answer('De Waag'))
Q1.answers[4].set_true(True)
Q1.add_answer(Answer('De Oude Kerk'))
Q1.add_answer(Answer('Universiteit van Amsterdam'))
Q1.add_answer(Answer('Sint-Nicolaaskerk'))
Q1.answers[0].alter_level(0.25)
Q1.answers[1].alter_level(0.25)
Q1.answers[2].alter_level(0.25)
Q1.answers[3].alter_level(0.25)
Q1.answers[4].alter_level(0.75)
Q1.answers[5].alter_level(0.75)
Q1.answers[6].alter_level(0.75)
Q1.answers[7].alter_level(0.75)
Q1.alter_category(natural_language_classifier.classify("3363cfx256-nlc-54927", Q1.name)['top_class'])

Q2 = Question('Who was commissioned to paint this painting of Dr. Nicolaes Tulp')
Q2.add_answer(Answer('Rembrandt van Rijn'))
Q2.answers[0].set_true(True)
Q2.add_answer(Answer('Johannes Vermeer'))
Q2.add_answer(Answer('Pieter Lastman'))
Q2.add_answer(Answer('Peter Paul Rubens'))
Q2.add_answer(Answer('Rembrandt'))
Q2.answers[4].set_true(True)
Q2.add_answer(Answer('Piet Mondriaan'))
Q2.add_answer(Answer('Fiep Westendorp'))
Q2.add_answer(Answer('Desiderius Erasmus'))
Q2.answers[0].alter_level(0.75)
Q2.answers[1].alter_level(0.75)
Q2.answers[2].alter_level(0.75)
Q2.answers[3].alter_level(0.75)
Q2.answers[4].alter_level(0.25)
Q2.answers[5].alter_level(0.25)
Q2.answers[6].alter_level(0.25)
Q2.answers[7].alter_level(0.25)
Q2.alter_category(natural_language_classifier.classify("3363cfx256-nlc-54927", Q2.name)['top_class'])

Q3 = Question('Why were the men wearing collars?')
Q3.add_answer(Answer('They were fashionable'))
Q3.answers[0].set_true(True)
Q3.add_answer(Answer('They were rich'))
Q3.add_answer(Answer('It looked nice in that time'))
Q3.answers[2].set_true(True)
Q3.add_answer(Answer('Because of their immense amount of swagger'))
Q3.add_answer(Answer('To prevent blood entering their clothes'))
Q3.answers[0].alter_level(0.75)
Q3.answers[1].alter_level(0.75)
Q3.answers[2].alter_level(0.25)
Q3.answers[3].alter_level(0.25)
Q3.answers[4].alter_level(0.25)
Q3.alter_category(natural_language_classifier.classify("3363cfx256-nlc-54927", Q3.name)['top_class'])

Q4 = Question('Which period is the painting from?')
Q4.add_answer(Answer('17e eeuw'))
Q4.answers[0].set_true(True)
Q4.add_answer(Answer('16e eeuw'))
Q4.add_answer(Answer('18e eeuw'))
Q4.add_answer(Answer('15e eeuw'))
Q4.add_answer(Answer('1632'))
Q4.answers[4].set_true(True)
Q4.add_answer(Answer('1623'))
Q4.add_answer(Answer('1631'))
Q4.add_answer(Answer('1648'))
Q4.answers[0].alter_level(0.25)
Q4.answers[1].alter_level(0.25)
Q4.answers[2].alter_level(0.25)
Q4.answers[3].alter_level(0.25)
Q4.answers[4].alter_level(0.75)
Q4.answers[5].alter_level(0.75)
Q4.answers[6].alter_level(0.75)
Q4.answers[7].alter_level(0.75)
Q4.alter_category(natural_language_classifier.classify("3363cfx256-nlc-54927", Q4.name)['top_class'])

try:
    name = input('What is your name?\n')
    player = Student(name)
    question_path = [Q1,Q2,Q3,Q4]
    player.age = int(input("How old are you? (Choose 13, 14 or 15)\n"))
    player.education = int(input("What is your educational level? (Choose 1 for VMBO, 2 for HAVO and 3 for VWO)\n"))
    player.interests = input('Enter your interests, separated by a comma.\n')
    player.interest_level = float(input('How interested are you in art on a scale from 1 to 10?\n'))/10
    print("Thanks {}, we're initializing the quiz for you \n".format(name))
except ValueError:
    sys.exit("Invalid value entered, restart the application.")

category = natural_language_classifier.classify("3363cfx256-nlc-54927", ' '.join(player.interests))['top_class']
first_questions = []
last_questions = []
for q in question_path:
    if q.category == category :
        first_questions.append(q)
    else:
        last_questions.append(q)

real_question_path = first_questions + last_questions

try:
    player_df = pd.DataFrame([player.education, player.age, player.interest_level, 0.0, 0.0, 0.0, 0.0, 0.0])
    i = 0
    for q in real_question_path:
        i += 1
        new_skill = np.clip(mlp.predict(player_df.transpose()), 0, 1)
        print("Your skill level is {}\n".format(round(new_skill[0],3)))
        print("Question {}: {}\n".format(i, q.name))
        if (new_skill < 0.5):
            a_skill_level = 0.25
        else:
            a_skill_level = 0.75
        j = 0
        correct = 0
        for a in q.answers:
            if a.level == a_skill_level:
                j += 1
                print("{}: {}".format(j, a.name))
                if a.is_true:
                    correct = j
                    correct_answer = a.name
        answer = int(input('Answer:'))
        if correct == answer:
            print("CORRECT!")
            player.num_correct += 1
        else:
            print("Unfortunately that was the wrong answer. The correct answer was: {}".format(correct_answer))
        fb = int(input("What did you think of the level of this question? (-1 for too hard, 0 for okay, 1 for too easy)\n"))
        player_df = pd.DataFrame([player.education, player.age, player.interest_level, i, player.num_correct/i, 60, new_skill, fb])
except ValueError:
    sys.exit("Invalid value entered, restart the application.")

print("You ended up with skill level {}".format(np.clip(round(mlp.predict(player_df.transpose())[0],3), 0, 1)))

## Code to train and validate the neural network
# skill_data = pd.read_csv('dataset_nn.csv', header=0
#                         ,  names=["education", "age", "interest", "num_of_questions", "perc_correct", "avg_time_to_answer", "prev_skill_level", "feedback", "pred_skill_level"])
#
#
# X = skill_data.drop('pred_skill_level', axis=1)
# y = skill_data['pred_skill_level']
# X_train, X_test, y_train, y_test = train_test_split(X, y)
# mlp.fit(X_train, y_train)
# predictions = mlp.predict(X_test)
# r2_score(y_test, predictions)


## Training the Natural Language Classifier
# with open("dataset_nlc.csv", 'rb') as training_data_nlc:
#     classifier = natural_language_classifier.create(training_data=training_data_nlc, name="InterestClassifier", language="en")

# natural_language_classifier.classify("3363cfx256-nlc-54927", "Watson")['top_class']
