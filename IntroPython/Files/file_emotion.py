text_file = open("../data/emotion_words2.txt", 'r')
## other code here that refers to variable fileref
num_lines = 0
for aline in text_file:
    num_lines += 1
print(num_lines)
text_file.close()
