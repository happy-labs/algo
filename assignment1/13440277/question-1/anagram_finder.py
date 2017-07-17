import os.path
import itertools


# use as a hash table to keep words in the file
anagram_dict = {}


def init_anagrams(file_name):
    """
    Load text content in 'words_anagram.txt' to hash table, (in to python dict)
    Purpose of storing in hash table is efficient lookup of strings

    Need to iterate over each and every line of the file and extract the
    content in to a hash table. There are no key value pairs in the text file.
    So store this words as keys and line no or may be empty string as a value

    Args:
        file_name - anagram text file(path to text file)
    """
    # keep world list in here
    anagram_list = []

    if os.path.isfile(file_name) or \
       1 == 1:
        # read file content to a list
        file = open(file_name, 'r')
        file_content = file.read()
        anagram_list = file_content.split()
        file.close()

        # iterate over word list and add words to dict
        for index, word in enumerate(anagram_list):
            anagram_dict[word] = index


def find_anagrams(text):
    """
    Find anagrams of given text and display it for clarification

    First need to identify all character combinations of given string. Then
    iterate through the combination list and check given sting is in anagram
    dictionary

    Args:
        text - input text to find anagrams
    """
    # keep anagrams and count
    anagram_count = 0
    anagram_list = []

    for word in list(map("".join, itertools.permutations(text))):
        # iterate over all combinations of given text
        if word != text:
            # we don't consider text as anagram
            if word in anagram_dict:
                anagram_count += 1
                anagram_list.append(word)

    # display anagrams
    if anagram_count > 0:
        print('text - %s' % text)
        print('anagram count - %d' % anagram_count)
        print('anagram list - %s' % anagram_list)
    else:
        print('No anagrams found')


if __name__ == '__main__':
    """
    Main method,

    This will execute very first, there are tow main functions that need to do
    in here
        1. Load content in anagram text file to hash table
        2. Listen for command line input texts and find anagrams of the input
           text
    """
    # load anagram file content
    file_name = 'words_anagram.txt'
    init_anagrams(file_name)

    # listen for command line input
    # find anagrams of input text
    while True:
        print('_______________________________________')
        input_text = raw_input('Enter text - ')
        find_anagrams(input_text)
        print('_______________________________________')
        print('\n')
