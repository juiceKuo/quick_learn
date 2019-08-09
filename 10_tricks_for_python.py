#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 23:27:01 2019

@author: ChihChi
"""

# 1-1
condition = True

if condition == True:
    x = 1
else:
    x = 0

print(x)

# 1-2
condition = True

x = 1 if condition else 0

print(x)


# 2-1
num_1 = 1000000000
num_2 = 1000000

total = num_1 + num_2
print(total)

# 2-2
num_1 = 1_000_000_000
num_2 = 1_000_000

total = num_1 + num_2
print(total)
print(f'{total:,}')

# 3-1
f = open('/Users/ChihChi/Documents/Learn_Python/text.txt', 'r')
file_content = f.read()
f.close()

words = file_content.split(' ')
word_count = len(words)
print(word_count)

# 3-2
with open('/Users/ChihChi/Documents/Learn_Python/text.txt', 'r') as f:
    file_content = f.read()


# 4-1
index = 0
names = ['Charlie', 'Ivy', 'Amanda', 'Burno']
for name in names:
    print(index, name)
    index += 1

# 4-2
names = ['Charlie', 'Ivy', 'Amanda', 'Burno']
for index, name in enumerate(names, start=1):
    print(index, name)
    
# 5-1
names = ['Peter Parker', 'Clark Kent', 'Wade Willson', 'Bruce Wayde']
heros = ['Spyder Man', 'Super Man', 'Dead Pool', 'Batman']

for index, name in enumerate(names):
    hero = heros[index]
    print(f'{name} is actually {hero}')
    
    
# 5-2
names = ['Peter Parker', 'Clark Kent', 'Wade Willson', 'Bruce Wayde']
heros = ['Spyder Man', 'Super Man', 'Dead Pool', 'Batman']
universies = ['MArvel', 'DC', 'Marvel', 'DC']
    
for name, hero, universe in zip(names, heros, universies):
    print(f'{name} is actually {hero} from {universe}')

for value in zip(names, heros, universies):
    print(value)
    
# 6-1
a, b = (1, 2)
print(a)
#print(b)

# 6-2
a, _ = (1, 2)
print(a)

# 7-1
a, b, c = (1, 2, 3, 4, 5)

a, b, *c = (1, 2, 3, 4, 5)

print(a)
print(b)
print(c)

# 7-2
a, b, *_ = (1, 2, 3, 4, 5)
print(a)
a, b, *_, d = (1, 2, 3, 4, 5, 6, 7)

print(a)
print(b)
#print(c)
print(d)
print(b)












    










