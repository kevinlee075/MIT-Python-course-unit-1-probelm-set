# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 15:00:04 2021

@author: Lenovo
"""

s = str(input('s = ')) #define s as an input string
Vowels = 0 #initial vowel
for letter in s: #examine whether s has vowels using loop
  if letter == 'a' or letter == 'e' or letter == 'i' \
     or letter == 'o' or letter == 'u': 
     Vowels += 1 #count vowels
print('Number of vowels: ' + str(Vowels)) #finally print number of vowels


s = str(input('s = ')) #define s as an input string
counts = 0 #initial counts
n = 0 #initial letter place
while n < len(s) - 2: #examine the place from '0' to 'third to last'
    if s[n] == 'b' and s[n+1] == 'o' and s[n+2] == 'b':
        #examine whether every three consecutive places are 'bob'
        counts += 1 #if yes, count one
        n += 1 #move to the next place
    else:
        n += 1 # if no, no count but move to the next place                            
print('Number of times bob occurs is: ' + str(counts)) #finally print results


s = str(input('s = ')) #define s as an input string
a = '' #define a as the checking place
b = '' #define b as the substring which should be memorized
for i in range(len(s)): #checking places from 0 to end
    a += s[i] #add every checking place first
    if len(a) > len(b): #memorize a if a is in order and follow the following check
        b = a 
    if i == len(s) - 1 and a == b + s[-1]: #check whether b is in the last substring
        b = a #if yes, the final letter should be added into b
    if i < len(s)-1:
        if s[i] > s[i+1]:
            a = ''    
print('Longest substring in alphabetical order is: ' + b)


    

        
        
