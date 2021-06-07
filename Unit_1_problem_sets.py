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


s = str(input('s = '))
counts = 0
n = 0
while n < len(s) - 1:
    if s[n] == 'b' and s[n+1] == 'o' and s[n+2] == 'b':
        counts += 1
        n += 1
    else:
        n += 1                            
print('Number of times bob occurs is: ' + str(counts))
    
    

        
        
