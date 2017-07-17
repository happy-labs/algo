import random
from utils import get_dna_string
from utils import match_pattern_and_text
from utils import get_age_category
from utils import is_alive


# file names
file_name1 = 'file1.txt'
file_name2 = 'file2.txt'
file_name3 = 'file3.txt'

# normal patterns
normal_pattern1 = 'ATGGA'
normal_pattern2 = 'TGGAC'
normal_pattern3 = 'CCGT'

# infected patterns
infected_pattern1 = 'AATTG'
infected_pattern2 = 'TTACC'
infected_pattern3 = 'GTTT'

# keep these flags to track file processed status
processed_file1 = False
processed_file2 = False
processed_file3 = False


def init_dna():
    """
    Generate three DNA text string from alphabet {A,C,G,T} These texts
    need to store in three different text file by depicting age groups.
    Age groups are below
        1. age >= 50
        2. 30 >= age > 50
        3. age < 30

    Each DNA string must contains at least 10,000 characters. Need to
    select random item from alphabet and put it in the file
    """
    # we only add alphabet characters to file
    alphabet = ['A', 'C', 'G', 'T']

    # write to 3 files
    file1 = open(file_name1, 'w')
    file2 = open(file_name2, 'w')
    file3 = open(file_name3, 'w')

    for i in range(0, 10000):
        file1.write(random.choice(alphabet))
        file2.write(random.choice(alphabet))
        file3.write(random.choice(alphabet))

    file1.close()
    file2.close()
    file3.close()


def approximate_age(dna_profile):
    """
    Approximate the age of give DNA string by analyzing it. Following are the
    relationships between age and patterns
        1. over 50 category - more sequences of ATGGA occur in DNA
        2. 30 to 50 category - more sequences of TGGAC occur in DNA
        3. below 30 category - more sequence of CCGT occur in DNA

    Need find the count of above three patterns('ATGGA', 'TGGAC', 'CCGT'),
    in order to identify the age

    Args:
        dna - DNA profile
    """
    matchers1 = 0
    matchers2 = 0
    matchers3 = 0

    # iterate over text to match the first two patterns
    for i in range(0, len(dna_profile) - len(normal_pattern1) + 1):
        text = dna_profile[i:len(normal_pattern1) + i]

        if match_pattern_and_text(text, normal_pattern1):
            matchers1 = matchers1 + 1

        if match_pattern_and_text(text, normal_pattern2):
            matchers2 = matchers2 + 1

    # iterate over text to match the third pattern
    for i in range(0, len(dna_profile) - len(normal_pattern3) + 1):
        text = dna_profile[i:len(normal_pattern3) + i]

        if match_pattern_and_text(text, normal_pattern3):
            matchers3 = matchers3 + 1

    # finally get the age category according to the matching count
    return get_age_category(matchers1, matchers2, matchers3)


def infect_dna(dna_profile, age_category):
    """
    Scan DNA profile and replace the specific patterns in the text. The
    replacements are doing according the below criteria
        1. if age > 50 replace ATGGA with AATTG
        2. if 30 < age < 50  replace TGGAC with TTACC
        3. if age < 30 replace CCGT with GTTT

    Args:
        dna_profile - dna string
        age_category - three age categories(we simplified categories as below)
        1 - age > 50
        2 - 30 < age < 50
        3 - age < 30

    Returns:
        infected dna profile
    """
    original_pattern = normal_pattern1
    infecting_pattern = infected_pattern1
    if age_category == 1:
        # replace ATGGA with AATTG
        original_pattern = normal_pattern1
        infecting_pattern = infected_pattern1
    elif age_category == 2:
        # replace TGGAC with TTACC
        original_pattern = normal_pattern2
        infecting_pattern = infected_pattern2
    else:
        # replace CCGT with GTTT
        original_pattern = normal_pattern3
        infecting_pattern = infected_pattern3

    # replace pattern
    return dna_profile.replace(original_pattern, infecting_pattern)


def detect_alive_status(infected_profile):
    """
    Detect person alive or dead. if infected pattern count exceed 200 person
    id dead. Following are the infected DNA patterns
        1. AATTG
        2. TTACC
        3. GTTA
    """
    # keep infected pattern count
    count = 0

    # one iteration to match 1st and 2nd patterns
    for i in range(0, len(infected_profile) - len(infected_pattern1) + 1):
        text = infected_profile[i:len(infected_pattern1) + i]

        if match_pattern_and_text(text, infected_pattern1):
            count = count + 1

        if match_pattern_and_text(text, infected_pattern2):
            count = count + 1

    # another iteration to match 3rd pattern(need to have another iteration
    # since the pattern length is not equal to first two patterns)
    for i in range(0, len(infected_profile) - len(infected_pattern3) + 1):
        text = infected_profile[i:len(infected_pattern3) + i]

        if match_pattern_and_text(text, infected_pattern3):
            count = count + 1

    # finally detect alive status according to the infected count
    is_alive(count)


if __name__ == '__main__':
    """
    Main method,

    This will execute very first
    """
    init_dna()

    # listen for command line input
    # we get file name from command line input
    while True:
        print('_______________________________________')
        # read dna from file
        file_name = raw_input('Enter file name - ')
        dna_profile = get_dna_string(file_name)

        # get age category and infect the dna
        age_category = approximate_age(dna_profile)
        infected_dna_profile = infect_dna(dna_profile, age_category)

        # find dead or alive
        detect_alive_status(infected_dna_profile)
        print('_______________________________________')
        print('\n')
