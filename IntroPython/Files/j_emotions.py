emotions = open("../data/emotion_words2.txt", 'r')
## other code here that refers to variable fileref
j_emotions = []
file = emotions.read()
words = file.split()
for item in words:
    if item[0] == 'j':
        j_emotions.append(item)
print("Emotions that begin with the letter j:", j_emotions)
emotions.close()
