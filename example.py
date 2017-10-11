
#Danielle Wilson
#Intro NLP: Assignment 3
#Due: October 10, 2017

"""
Doctests:

>>> has_most_consonants('The door is closed. And many dogs barked.')
['closed.', 'barked.']
>>> has_most_consonants('The door is closed. And many dogs barked. Closed')
['closed.', 'barked.']
>>> has_most_consonants('')
[]

>>> is_determiner('the')
True
>>> is_determiner('thesis')
False
>>> is_determiner('The')
True

>>> remove_determiners('the dog is asleep in a basket.')
'dog is asleep in basket.'

>>> lst = [['a', 'big', 'red', 'dog'], ['chased', ['a', 'small', 'red', 'cat']]]
>>> replace_word(lst, 'a', 'the')
[['the', 'big', 'red', 'dog'], ['chased', ['the', 'small', 'red', 'cat']]]

>>> bigrams = get_bigrams('The dog is asleep in a basket? Yes, in a basket!')
>>> sorted(bigrams.items())[:4]
[((',', 'in'), 1), (('?', 'yes'), 1), (('a', 'basket'), 2), (('asleep', 'in'), 1)]

>>> trigrams = get_trigrams('The dog is asleep in a basket? Yes, in a basket!')
>>> sorted(trigrams.items())[:3]
[((',', 'in', 'a'), 1), (('?', 'yes', ','), 1), (('a', 'basket', '!'), 1)]

>>> ngrams = get_ngrams('The dog is asleep in a basket? Yes, in a basket!', 2)
>>> sorted(ngrams.items())[:4]
[((',', 'in'), 1), (('?', 'yes'), 1), (('a', 'basket'), 2), (('asleep', 'in'), 1)]
>>> ngrams = get_ngrams('The dog is asleep in a basket? Yes, in a basket!', 3)
>>> sorted(ngrams.items())[:3]
[((',', 'in', 'a'), 1), (('?', 'yes', ','), 1), (('a', 'basket', '!'), 1)]

"""

#PROBLEM 1.
"""
For this exercise,
consonants are just letters like t and k (in fact, all letters except a, e, i, o
and u). You may use split() to get the tokens and you do not need to worry about
splitting off punctuations. 
"""

def has_most_consonants(string):
    """ has_most_consonants() takes a string as input and returns
    the words that have the largest number of consonants in them."""
    
    from operator import itemgetter
    
    if string == '':
        return []
    
    tokens = string.split()
    #creates a dictionary with words & their # of consonants
    consonantDict = {}
    for word in tokens:
        score = 0
        for letter in word:
            if letter not in 'aeiou':
                score += 1
        consonantDict[word] = score

    # sorts dictionary by score highest to lowest
    sortMostCons = sorted(consonantDict.items(), key=itemgetter(1), reverse=True)
    # gets word with highest score
    highest = sortMostCons[0][1]
    # checks if there are any other words with that score
    # and appends them to the result
    result = []
    for item in sortMostCons:
        if item[1] == highest:
           result.append(item[0])
    return result

#PROBLEM 2.

def is_determiner(word):
    """ is_determiner() takes a word as input and decides
    if it is a determiner."""
    
    return word in 'The the A a An an'


def remove_determiners(text):
    """ remove_determiners() uses is_determiner() and eliminates all determiners in a
    piece of a text.
    Contrary to what I said in class, do not worry about punctuation. But do worry
    about removing things like 'The'.    """

    tokens = text.split()
    result = []
    # appends elements that aren't determiners to a list
    for i in range(len(tokens)):
        if is_determiner(tokens[i]) != True:
            result.append(tokens[i])
    # turns the list back into a string        
    result_string = ' '.join(result)
    return result_string


#PROBLEM 3.
"""
Given an embedded list such as

   [['a', 'big', 'red', 'dog'], ['chased', ['a', 'small', 'red', 'cat']]]

where the embedding can be of any depth, but where the contents of the lists are
either other lists or strings.

"""

def replace_word(lst, find, replace):
    """replace all instances of an
    arbitrary word with a new word."""

    # loops through list
    for i in range(len(lst)):
        # if the current element is the thing to replace
        if lst[i] == find:
            lst[i] = replace
        # if the current element is a list
        elif isinstance(lst[i], list):
            replace_word(lst[i], find, replace)
        # if element doesn't need to change
        else:
            return replace_word(lst[i+1:], find, replace)
    return lst
            

#PROBLEM 4.
"""As part of this, split off end-of-sentence
punctuation markers and commas and put all words in lower case. You can reuse
part of your solution to assignment 2 here.
"""

def tokenize(string):
    """takes a string and splits it up into words and punctuation.
    returns a list of each element"""
    
    split = string.split()
    punctuation = '.?!:;,'
    tokens = []
    for word in split:
        # if connected to punctuation, splits up the word & punct
        if word.endswith(".") or word.endswith("?") or word.endswith("!") or word.endswith(":") or word.endswith(";") or word.endswith(","):
            tokens.append(word[0:len(word)-1])
            tokens.append(word[len(word)-1])
        else:
            tokens.append(word)

    lower_tokens = list(word.lower() for word in tokens)
    return lower_tokens

def get_bigrams(string):
    """takes a string as input and returns a dictionary of
    bigrams and their frequencies."""
    
    lower_tokens = tokenize(string)
    bigrams = {}
    for i in range(len(lower_tokens)-1):
        #makes tuple of the word and the following word
        word_pair = (lower_tokens[i], lower_tokens[i+1])
        if word_pair not in bigrams.keys():
            bigrams[word_pair] = 1
        else:
            bigrams[word_pair] = bigrams[word_pair]+1
    
    return bigrams

"""
In addition, write a similar function for trigrams.

"""
def get_trigrams(string):
    """takes a string as input and returns a dictionary of
    trigrams and their frequencies."""
    
    lower_tokens = tokenize(string)
    
    trigrams = {}
    for i in range(len(lower_tokens)-2):
        #makes tuple of word with the 2 following words
        word_pair = (lower_tokens[i], lower_tokens[i+1], lower_tokens[i+2])
        if word_pair not in trigrams.keys():
            trigrams[word_pair] = 1
        else:
            trigrams[word_pair] = trigrams[word_pair]+1
    
    return trigrams
 

#PROBLEM 5 (extra credit).
""" Makes sure that this works for any integer higher than 1, not just bigrams and
trigrams. This means you need to give a meaningful message for those cases where
ngrams would be longer than the text itself.
"""

def get_ngrams(string, n):
    """Write a function that takes as input a string and a number (the number being the
    n in ngrams) and returns a dictionary of ngrams and their frequencies. """
   
    lower_tokens = tokenize(string)

    if n > len(lower_tokens):
        print("Error: number larger than length of input")
        return None
    
    ngrams = {}
    for i in range(len(lower_tokens)-(n-1)):
        #makes tuple of n length
        word_group = tuple(lower_tokens[i:i+n])
        if word_group not in ngrams.keys():
            ngrams[word_group] = 1
        else:
            ngrams[word_group] = ngrams[word_group]+1
    
    return ngrams


if __name__ == '__main__':

    import doctest
    doctest.testmod()
