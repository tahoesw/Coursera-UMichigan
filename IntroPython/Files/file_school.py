school = open("../data/school_prompt2.txt", 'r')
## other code here that refers to variable fileref
chars = school.read()
num_chars = len(chars)
print(num_chars)
school.close()
