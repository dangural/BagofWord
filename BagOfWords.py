import numpy as np


def my_bag_of_words(text, words_to_index, dict_size):
    """
        text: a string
        dict_size: size of the dictionary
        words_to_index: words in our dictionary (hi, you, me, are)
        return a vector which is a bag-of-words representation of 'text'
    """
    popWords=dict.fromkeys(words_to_index)
    for index, word in enumerate(popWords.keys()):
        popWords[word] = index;

    result_vector = np.zeros(dict_size)

    textList = list(text.split(' '))

    for index, word in enumerate(textList):
        if word in popWords:
            result_vector[popWords[word]] += 1
    return result_vector

text = 'hi how are you'
words_to_index = ['hi','you','me','are']
dict_size=4

print(my_bag_of_words(text,words_to_index,dict_size))