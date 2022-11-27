punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
def get_positive_words():
    positive_words = []
    with open("../data/positive_words.txt") as pos_f:
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                positive_words.append(lin.strip())
    return positive_words

def get_negative_words():
    negative_words = []
    with open("../data/negative_words.txt") as pos_f:
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                negative_words.append(lin.strip())
    return negative_words

def strip_punctuation(s):
    for char in punctuation_chars:
        s = s.replace(char, "")
    return s

def get_count_of_positive_words_in_tweet(s):
    positives = 0
    for word in s.split():
        word = strip_punctuation(word)
        if word.lower() in positive_words:
            positives += 1
    return positives

def get_count_of_negative_words_in_tweet(s):
    negatives = 0
    for word in s.split():
        word = strip_punctuation(word)
        if word.lower() in negative_words:
            negatives += 1
    return negatives

positive_words = get_positive_words()
negative_words = get_negative_words()

in_fileconnection = open("../data/project_twitter_data.csv", 'r')
out_fileconnection = open("../data/resulting_data.csv", "w")
# output the header row
out_fileconnection.write('Number of Retweets,Number of Replies,Positive Score,Negative Score,Net Score')
out_fileconnection.write('\n')

lines = in_fileconnection.readlines()
header = lines[0]
field_names = header.strip().split(',')
print(field_names)
for row in lines[1:]:
    if row[len(row) - 1] == '\n':
        print(row[0:len(row) - 1])
    else:
        print(row[0:len(row)])
    #pull out indiv fields
    vals = row.strip().split(',')
    pos_count = get_count_of_positive_words_in_tweet(vals[0])
    neg_count = get_count_of_negative_words_in_tweet(vals[0])
    score = pos_count - neg_count
    num_retweets = vals[1]
    num_replies  = vals[2]
    print_row_string = 'num_retweets {}, num_replies {}, pos_count {}, neg_count {}, score {}'.format(num_retweets,
                                         num_replies, pos_count, neg_count, score)
    print(print_row_string)
    print()
    row_string = '{},{},{},{},{}'.format(num_retweets, num_replies,
                                         pos_count, neg_count, score)
    out_fileconnection.write(row_string)
    out_fileconnection.write('\n')
