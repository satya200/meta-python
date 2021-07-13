#!/usr/bin/env python3

words = ['one', 'two', 'three']

n = 0
while(n < 3):
    print(words[n])
    n += 1

for i in words:
    print(i)

secret = 'satya'
pw = ''

while pw != secret:
    pw = input('Input is not matching?')
