text = open("../data/emotion_words2.txt", 'r')
## other code here that refers to variable fileref
first_forty = text.read(40)
print(first_forty)
text.close()
