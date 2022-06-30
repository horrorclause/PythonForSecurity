#!/usr/bin/python3

"""
Codewars: Simple Pig Latin
"""

import string

def pig_it(text):
    latin = []
    try:
        for word in text.split():
            if word not in string.punctuation:
                latin.append(word[1:] + word[0] + "ay")
            else:
                punct = word
        latin.append(punct)
    except:
        pass
    return " ".join(latin)
