# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 15:00:04 2021

@author: Lenovo
"""

s = str(input('s = '))
Vowels = 0
for letter in s:
  if letter == 'a' or letter == 'e' or letter == 'i' \
     or letter == 'o' or letter == 'u':
     Vowels += 1 #hehe
print('Number of vowels: ' + str(Vowels))