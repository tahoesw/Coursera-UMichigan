travel = open("../data/travel_plans2.txt", 'r')
## other code here that refers to variable fileref
lines = travel.readlines()
num_lines = len(lines)
print(num_lines)
travel.close()
