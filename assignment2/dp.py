def dynamic(text, width):
    words = text.split()
    count = len(words)
    slack = [[0] * count for i in range(count)]
    for i in range(count):
        print i
        slack[i][i] = width - len(words[i])
        for j in range(i + 1, count):
            slack[i][j] = slack[i][j - 1] - len(words[j]) - 1

    minima = [0] + [10 ** 20] * count
    breaks = [0] * count
    for j in range(count):
        i = j
        while i >= 0:
            if slack[i][j] < 0:
                cost = 10 ** 10
            else:
                cost = minima[i] + slack[i][j] ** 2
            if minima[j + 1] > cost:
                minima[j + 1] = cost
                breaks[j] = i
            i -= 1
    print '-----------------------------------------------------------------'
    print 'Input words : %s ' % words
    print 'Margin width : %d \n' % width

    lines = []
    j = count
    print 'minima %s' % minima
    print 'breaks %s' % breaks
    while j > 0:
        i = breaks[j - 1]
        lines.append(' '.join(words[i:j]))
        j = i
    lines.reverse()

    print 'Output :'
    for i in range(len(lines)):
        print lines[i]
    print '-----------------------------------------------------------------'

    print '\n'
    print slack

    print '\n'
    print words
    print '\n'

    for i in range(len(slack)):
        print slack[i]


#dynamic('aaa bb cc ddddd', 6)
#print '--------------------'
#s = 'One could imagine some of these features being contextual'
s = 'She is happy but is a blue gal. I am all gone.'
#s = 'aaa'
dynamic(s, 15)


def init_slack(words, width):
    """
    Initialize slack, two diementional array, the content of the slack use to
    find the line break words. Slack function would be
                    |M| - |Wi|              if i = j

        S(i, j) =

                    S(i, j-1) - 1 - |Wj|    otherwise

    Args:
        words - list of words in the paragraph
        width - max line width(|M|)
    """
    # n*m array
    count = len(words)
    slack = [[0] * count for i in range(count)]
    for i in range(count):
        slack[i][i] = width - len(words[i])
        for j in range(i + 1, count):
            slack[i][j] = slack[i][j - 1] - len(words[j]) - 1

    return slack


def find_best(words, width):
    """
    Find the best line breaks from input word list according to dynamic
    dynamic programming properties. We are using the content in slck function
    to calculate the best(i)

        for k -> 0 to n
            min {Best (k) + (S(k+1), n) ^ 3}
    """
    print 'Input words : %s' % words

    # initilaize slack first
    slack = init_slack(words, width)

    # ierate over character count and apply
    count = len(words)
    minima = [0] + [10 ** 20] * count
    breaks = [0] * count
    for j in range(count):
        i = j
        while i >= 0:
            if slack[i][j] < 0:
                cost = 10 ** 10
            else:
                cost = minima[i] + slack[i][j] ** 2
            if minima[j + 1] > cost:
                minima[j + 1] = cost
                breaks[j] = i
            i -= 1

    return breaks
