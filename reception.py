import speech_recognition as sr
import en_core_web_sm
import os
import spacy
from spacy import displacy
from spacy.symbols import NOUN, NUM

from nltk import Tree


def to_nltk_tree(node):
    if node.n_lefts + node.n_rights > 0:
        return Tree(node.orth_, [to_nltk_tree(child) for child in node.children])
    else:
        return node.orth_

intro_speech = 'Hello and welcome to our hotel. Do you have reservation?'
os.system('espeak "{}"'.format(intro_speech))

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    textT = r.recognize_google(audio)
    #print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

print(str(textT))
if (textT.lower() == "yeah" or textT.lower() == "yes"):
    yes_reservation_speech = 'Can I get your passports so that I can register and prepare your room.'
    os.system('espeak "{}"'.format(yes_reservation_speech))
    exit

room_menu_options = 'OK. No worries. Your options for rooms are'
os.system('espeak "{}"'.format(room_menu_options))

room_options = ['single room for 10 euro', 'double room for 20 euro', 'king suite for 50 euro']
for h_room in room_options:
    os.system('espeak "{}"'.format(h_room))


people_req = 'How many people are you?'
os.system('espeak "{}"'.format(people_req))

# obtain audio from the microphone
r2 = sr.Recognizer()
with sr.Microphone() as source2:
    print("Say something!")
    audio2 = r2.listen(source2)

# recognize speech using Google Speech Recognition
try:
    people_selection = r.recognize_google(audio2)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


nlp = en_core_web_sm.load()
doc1 = nlp(people_selection)
nums = []
for possible_subject in doc1:
    if possible_subject.pos == NUM:
        nums.append(possible_subject.text)


requestedPeople=int(nums[0])
print(nums[0])

if(requestedPeople > 2):
    doubleRoom = requestedPeople / 2
    singleRoom = requestedPeople % 2
    suggest1_options = "OK. I can suggest you "+str(int(doubleRoom))+" double room and"+str(int(singleRoom))+"single room"
    os.system('espeak "{}"'.format(suggest1_options))
else:
    suggest2_options = 'OK. I can suggest you single room or highly luxurious king suite'
    os.system('espeak "{}"'.format(suggest2_options))


print("------------------------")
for token in doc1:
    print(token.text, token.pos_, token.dep_)
    print("------------------------")

print("Dependency Tree")
[to_nltk_tree(sent.root).pretty_print() for sent in doc1.sents] # Dependency tree

#########################



order_req = 'So what you want to reserve?'
os.system('espeak "{}"'.format(order_req))

# obtain audio from the microphone
r3 = sr.Recognizer()
with sr.Microphone() as source3:
    print("Say something!")
    audio3 = r3.listen(source3)

# recognize speech using Google Speech Recognition
try:
    room_selection = r.recognize_google(audio3)
    #print("xxxxx: "+room_selection)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


nlp = en_core_web_sm.load()
doc = nlp(room_selection)
for token in doc:
    print(token.text, token.pos_, token.dep_)
    print("------------------------")

print("Dependency Tree")
[to_nltk_tree(sent.root).pretty_print() for sent in doc.sents] # Dependency tree

print("------------------------")
room_adj_noun=[]
for i in nlp(room_selection):
    if i.pos_ in ["NOUN", "PROPN"]:
        comps = [j for j in i.children if j.pos_ in ["ADJ", "NOUN", "PROPN"]]
        if comps:
            
            str1 = ""
            adj_selection = ','.join(str(v) for v in comps)
            room_adj_noun.append(adj_selection+" "+str(i))
            


print("------------------------")
str1 = " "
room_adj_noun_str=str1.join(room_adj_noun)
print("Requested: "+room_adj_noun_str)


if(room_adj_noun_str == 'single room'):
    totalCost = requestedPeople * 10
    suggest1_options = "I have prepared your single room with the price of"+str(int(totalCost))
    os.system('espeak "{}"'.format(suggest1_options))
elif(room_adj_noun_str == 'double room'):
    totalCost = doubleRoom * 20 + singleRoom * 10
    suggest1_options = "I have prepared your double room with the price of"+str(int(totalCost))
    os.system('espeak "{}"'.format(suggest1_options))
elif(room_adj_noun_str == 'king suite'):
    totalCost = requestedPeople * 50
    suggest1_options = "I have prepared your king suite with the price of"+str(int(totalCost))
    os.system('espeak "{}"'.format(suggest1_options))
else:
    os.system('espeak "I am sorry what you said is not appliable."')