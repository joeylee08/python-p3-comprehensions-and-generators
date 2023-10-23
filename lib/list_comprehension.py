#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentence_list):
    return [string + "!" for string in sentence_list]

print(return_evens([1, 2, 3, 4, 5, 6, 7, 8]))
print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))

# python lib/list_comprehension.py