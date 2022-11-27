travel = open("../data/travel_plans2.txt", 'r')
## other code here that refers to variable fileref
destination = []
lines = travel.readlines()
for line in lines:
    if ':' in line:
        destination.append(line[0:-1])
print("list of destinations", destination)
travel.close()
