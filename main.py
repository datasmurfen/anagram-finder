#!/usr/bin/env python3
# -*- coding: utf-8 -*-

 
def createWordArray(filepath):
    with open(filepath, encoding="ISO-8859-1") as tf:
        wordarray = tf.readlines()
    return wordarray



counter = 0


def isAnagram(word1, word2):
    w1 = sorted(word1.rstrip())
    w2 = sorted(word2.rstrip())
    global counter
    if word1 == word2:
        pass
    elif w1 == w2:
        counter+=1
        print("{} ---- {} and {} are anagrams".format(counter, word1.rstrip(), word2.rstrip()))
        
          
    else:
        pass


 
if __name__ == "__main__":
    words = createWordArray("anagramlist.txt")
    for word in words:
        for word2 in words:
            isAnagram(word, word2)


