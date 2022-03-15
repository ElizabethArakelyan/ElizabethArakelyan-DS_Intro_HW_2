# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 14:35:11 2022

@author: eliza
"""


sentence = input("please write a sentence:")
word = input("please write a word:")
def reverse(sentence,word):
    sentence=sentence.lower()
    word=word.lower()
    a=0
    b=0
    if isinstance(word,str):
        if word in sentence:
            while a<len(word):
                if word[a]==sentence[b]:
                    return sentence.replace(word,word[::-1])
                    a=a+1
                    b=b+1
                else:
                    b=b+1
        else:
            return "The word was not found"
    else:
        return "invalid input" 
            
    
print(reverse(sentence,word))