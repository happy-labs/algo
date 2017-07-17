import os.path


def calculate_prefix(pattern):
    """
    Calculate prefix function of the pattern. the function output can be use
    in KMP shifts.

    Args:
        pattern - matching pattern

    Returns:
        list of prefix values
    """
    # keep pattern in a list
    pattern = list(pattern)

    prefixes = [1] * (len(pattern) + 1)
    shift = 1
    for pos in range(len(pattern)):
        while shift <= pos and pattern[pos] != pattern[pos - shift]:
            shift += prefixes[pos - shift]
        prefixes[pos + 1] = shift


def get_hash(text):
    """
    Get hash value of given text, we are using simple hash function to
    calculate hash value of given text

    Args:
        text - hashing text

    Returns:
        hash value of text
    """
    # we store alphabet in dictionary to obtain simple hash table
    hash_table = {}
    hash_table['A'] = 1
    hash_table['C'] = 2
    hash_table['G'] = 3
    hash_table['T'] = 4

    # just create hash value of text by sum up hash values of each and very
    # character in text
    hash_value = 0
    for char in text:
        hash_value += hash_table[char]

    return hash_value


def get_dna_string(file_name):
    """
    DNA strings storing in files, need to read the file in order to get the
    DNA string(we storing dna string in 'file1.txt', 'file2.txt', 'file3.txt')

    Args:
        file - file name

    Returns:
        DNA string
    """
    if os.path.isfile(file_name):
        # read file content to a list
        file = open(file_name, 'r')
        file_content = file.read()
        file.close()

        return file_content

    return None


def match_pattern_and_text(text, pattern):
    """
    Match the pattern and text, first need to check weather the hash values of
    pattern and text is equal. If they are equal we
    need to exact match the pattern and text

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


def get_age_category(count1, count2, count3):
    """
    Calculate the age category according to the matching count. Following are
    the criteria of matching count and age
        1. over 50 category - more sequences of ATGGA occur in DNA
        2. 30 to 50 category - more sequences of TGGAC occur in DNA
        3. below 30 category - more sequence of CCGT occur in DNA

    Args:
        count1 - no of 'ATGGA' pattern in DNA string
        count2 - no of 'TGGAC' pattern in DNA string
        count3 - no of 'CCGT' pattern in DNA string

    Returns:
        age category(use simplified categories)
        1 - age > 50
        2 - 30 < age < 50
        3 - age < 30
    """
    print("Pattern ATGGA count - %d" % count1)
    print("Pattern TGGAC count - %d" % count2)
    print("Pattern CCGT count - %d" % count3)

    max_count = max(count1, count2, count3)
    age_category = 1
    if max_count == count1:
        # over 50
        age_category = 1
        print("Age category - %s" % "over 50 range")
    elif max_count == count2:
        # 30 to 50 range
        age_category = 2
        print("Age category - %s" % "30 to 50 range")
    else:
        # below 30
        age_category = 3
        print("Age category - %s" % "below 30 range")

    return age_category


def is_alive(infected_count):
    """
    Check weather peron live or dead according to the infected count, if
    infected count exceed 200 person dead
    """
    if infected_count > 200:
        print ('Infected count exceed 200 - DEAD')
    else:
        print ('Infected count not exceed 200 - ALIVE')
