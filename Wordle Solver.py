#!/usr/bin/env python
# coding: utf-8

# In[31]:


import numpy as np


# In[61]:


import pandas as pd
import random 
import string


# In[116]:


def load_words( ): 
       print("Loading word list from file...")
       inFile = open('/Users/cbressler/Downloads/FiveLetterWords.csv', 'r') 
       line = inFile.readline( ) 
       wordlist = str.split(line) 
       print(" ", len(wordlist), "words loaded.")
       return wordlist

def choose_word (wordlist): 
       return random.choice (wordlist)

wordlist = load_words( )


# In[86]:


from striprtf.striprtf import rtf_to_text
with open('/Users/cbressler/Downloads/FiveLetterWords.csv', 'r') as infile:
    content = infile.read()
    text = rtf_to_text(content)
print(text[1] + text[2] + text[3])


# In[115]:


df = pd.read_csv('/Users/cbressler/Downloads/FiveLetterWords.csv')
#df = list(df)
#x = len(df)
#a = 0
#df2 = []
#while a < x:
    #df2 = df2 + str(df[a])
    #a = a + 1
a = open('/Users/cbressler/Downloads/FiveLetterWords.csv', 'r')
content = a.read()
b = 0
x = len(content)
word_list = []

for i in content:
    word_list.append(i)
#d = word_list[5] + word_list[1] + word_list[2] + word_list[3] + word_list[4]
while b < x - 5:
    c = (b * 6) + 1
    d = word_list[c] + word_list[c+1] + word_list[c+2] + word_list[c+3] + word_list[c+4]
    word_list[b] = d
    b = b + 1

#word_list[b] = d
word_list
#content[1] + content[2] + content[3] + content[4] + content[5]
    
    


# In[36]:


a = open('/Users/cbressler/Downloads/FiveLetterWords.csv', 'r')
word_list = a.read()
word_list = word_list.split(",")
number = input("Pick a number, 1-8937:")
number = int(number)
word_list


# In[40]:


a = open('/Users/cbressler/Downloads/FiveLetterWords.csv', 'r')
word_list = a.read()
word_list = word_list.split(",")
end_game = 0
while end_game == 0:
    word_guess = input("What word did you guess? ")
    correct = input("Was it right? (y/n) ")
    if correct == "y":
        end_game = restart()
    else:
        word_removal(word_guess,word_list)
    


# In[39]:


def restart():
    play_again = input("Congrats! Try Again? (y/n) ")
    if play_again == "y":
        end = 0
    else:
        print("Thanks for playing!")
        end = 1
    return(end)

def word_removal(word, wordlist):
    a = 0
    letter_1_result = int(input("what was the first letter? (1 = green, 2 = yellow, 3 = gray): "))
    letter_2_result = int(input("what was the second letter? (1 = green, 2 = yellow, 3 = gray): "))
    letter_3_result = int(input("what was the third letter? (1 = green, 2 = yellow, 3 = gray): "))
    letter_4_result = int(input("what was the fourth letter? (1 = green, 2 = yellow, 3 = gray): "))
    letter_5_result = int(input("what was the fifth letter? (1 = green, 2 = yellow, 3 = gray): "))
    if letter_1_result == 1 and letter_2_result == 1 and letter_3_result == 1 and letter_4_result == 1 and letter_5_result == 1:
        restart()
    else:
        wordlist = letter_finder(0, word[0],letter_1_result,wordlist)
        wordlist = letter_finder(1, word[1],letter_2_result,wordlist)
        wordlist = letter_finder(2, word[2],letter_3_result,wordlist)
        wordlist = letter_finder(3, word[3],letter_4_result,wordlist)
        wordlist = letter_finder(4, word[4],letter_5_result,wordlist)
    
def letter_finder(pos,char,result,wordlist):
    a = 0
    if result == 1:
        while a < len(wordlist):
            if wordlist[a][(pos - 1)] != char:
                wordlist.pop(a)
                a = a + 1           
    elif result == 2:
        while a < len(wordlist):
            if wordlist[a][(pos - 1)] == char:
                wordlist.pop(a)
                a = a + 1
            elif char not in wordlist[a]:
                wordlist.pop(a)
                a = a + 1
    elif result == 3:
        while a < len(wordlist):
            if char in wordlist[a]:
                wordlist.pop(a)
                a = a + 1
    return(wordlist)     
    
        
    


# In[44]:


x = df[20]
print(df)


# In[ ]:


def word_contains(letter):
    for x in df:
        if 

