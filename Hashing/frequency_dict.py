# Frequency Dictionaries in Python
# A frequency dictionary (also called a frequency map) in Python is a way to store and track the count (or frequency) of occurrences of specific elements in a dataset, such as a list, string, or iterable. It's essentially a dictionary where:

# Keys represent the unique elements (e.g., words, characters, numbers).
# Values represent the number of times each key appears.

# Example: Count the frequency of words in a sentence.
# Method 1: Using a for loop to iterate through the words and update the frequency dictionary.

def word_frequency(sentence):
    # Split the sentence into words
    words = sentence.lower().split()
    
    # Initialize an empty frequency dictionary
    frequency_dict = {}
    
    # Iterate through each word in the list
    for word in words:
        # If the word is already in the dictionary, increment its count
        if word in frequency_dict:
            frequency_dict[word] += 1
        # If the word is not in the dictionary, add it with a count of 1
        else:
            frequency_dict[word] = 1
            
    return frequency_dict

sentence = "the quick brown fox jumps over the lazy dog"
frequency = word_frequency(sentence)
print(frequency)


# Example: Count the frequency of numbers in a list.
# Method 2: Using the get() method of dictionaries to simplify the code.
# def number_frequency(numbers):
#     frequency_dict = {}
#     n = len(numbers)
#     for i in range(n):
#         frequency_dict[numbers[i]] = frequency_dict.get(numbers[i], 0) + 1
#     return frequency_dict

# nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# print(number_frequency(nums))


# Example: Count the frequency of characters in a string.
# Method 3: Using the collections.Counter class for a more concise solution.

# from collections import Counter

# def char_frequency(string):
#     return Counter(string)

# text = "hello"
# print(char_frequency(text))
    