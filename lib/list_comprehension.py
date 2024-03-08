#!/usr/bin/env python3

def return_evens(num_list):
    '''
    if len(num_list) == 0:
        print(list())
        return list()
    elif len(num_list) > 0:
    '''
    # Use one line(list comprehension) instead.
    even_numbers = [n for n in num_list if len(num_list) > 0 and n%2 == 0]
    print(even_numbers)
    return(even_numbers)
    pass

# Test cases
return_evens([]) # []
return_evens([0, 1, 3, 5, 7, 8, 9]) # [0, 8]

def make_exclamation(sentence_list):
    '''
    if len(sentence_list) == 0:
        print(list())
        return list()
    elif len(sentence_list) > 0:
    '''
    # write in one line(list comprehension) instead
    new_sentence_list = [f"{s}!" for s in sentence_list if len(sentence_list) > 0]
    print(new_sentence_list)
    return new_sentence_list
    pass

# Test cases
make_exclamation([])
make_exclamation(["Hello", "I'm doing great", "Python is fun"])
# ["Hello!", "I'm doing great!", "Python is fun!"]
