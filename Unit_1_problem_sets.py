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

s = 'feasbobwduvelm3bnsdfbowefbobdfjewkeweu'
counts = 0
for letter in s:
    if 'bob' in letter:
        counts += 1
print('Number of times bob occurs is: ' + str(counts))

        
        
