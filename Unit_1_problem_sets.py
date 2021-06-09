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
if s[0] <= s[1]:
    for m in range(1, len(s)):
        if s[m] <= s[m+1]:
            a = s[0:m+2]
        else:
            a = s[0:m+1]
            break
for n in range(1, len(s)):
    if s[n-1] > s[n] and s[n] <= s[n+1]:
        break
for o in range(n, len(s)):
    if s[o] <= s[o+1]:
        c = s[n:o+2]
    else:
        c = s[n:o+1]
        break
for p in range(o+1, len(s)):
    if s[p-1] > s[p] and s[p] <= s[p+1]:
        break
for q in range(p, len(s)):
    if s[q] <= s[q+1]:
        d = s[p:q+2]
    else:
        d = s[p:q+1]
        break
if len(a) >= len(c) and len(a) >= len(d):
    print('Longest substring in alphabetical order is: ' + a)
elif len(c) > len(a) and len(c) >= len(d):
    print('Longest substring in alphabetical order is: ' + c)
else:
    print('Longest substring in alphabetical order is: ' + d)


    

        
        
