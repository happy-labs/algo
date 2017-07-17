#keep hash values of pattern characters
hash_table = {}


def init_hash_table(pattern):
    """
    Initialize content in the hash table according to the pattern texts, need
    to iterate over pattern and add the text in to hash table. We use this hash
    table values when matching text and pattern. Add char as the key and index
    as the value on hash table

    Args:
        pattern - pattern to be match
    """
    for i in range(0, len(pattern) - 1):
        # fill hash table
        hash_table[pattern[i]] = i


def search_pattern(text, pattern):
    """
    Search a given pattern in the text. Search algorithm is Rabin-Karp.
    Advantage of using Rabin-Karp is, its capable to process incoming
    text(characters) in a constant amount of time. Actually Rabin-Karp
    algorithms hash value generating function should have capable for it

    Args:
        text -  incoming text
        pattern - matching pattern
    """
    print('Matching text - %s' % text)
    print('Matching pattern - %s' % pattern)

    for i in range(0, len(text) - len(pattern) + 1):
        # match sub string of pattern
        if match_pattern_and_text(text[i:len(pattern) + i], pattern):
            print('Pattern found at index %d' % i)


def match_pattern_and_text(text, pattern):
    """
    Match the pattern and text, first need to check weather the hash values of
    pattern and text is equal(according to Rabin-Karp). If they are equal we
    need to iterate over each and every character in text and check weather
    text is matching to the pattern

    Args:
        text - matching text
        pattern - matching pattern

    Returns:
        matching or not
    """
    if get_hash(text) == get_hash(pattern):
        for i in range(0, len(text)):
            if text[i] != pattern[i]:
                return False
    else:
        return False

    return True


def get_hash(text):
    """
    Get hash value of given text, we are using simple hash function to
    calculate hash value of given text

    Args:
        text - hashing text

    Returns:
        hash value of text
    """
    # just create hash value of text by sum up hash values of each and very
    # character in text
    hash_value = 0
    for char in text:
        if char in hash_table:
            hash_value += hash_table[char]
        else:
            return 0

    return hash_value


if __name__ == '__main__':
    """
    Main method,

    This will execute very first
    """
    pattern = ''
    text = ''

    # initially get pattern from command line input
    # initialize hash table of pattern
    pattern = raw_input('Enter a pattern to match - ')
    init_hash_table(pattern)

    # listen for command line input for matching texts
    while True:
        print('_______________________________________')

        # append text and search the pattern in text
        input = raw_input('Enter text to match [%s] - ' % text)
        text += input

        # match pattern and text
        search_pattern(text, pattern)
        print('_______________________________________')
        print('\n')
