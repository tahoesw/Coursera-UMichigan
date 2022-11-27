olypmicsfile = open("/Users/wel51x/Box/MyBox/Courses/Coursera/UMich/projects/IntroPython/data/olympics.txt", 'r')
## other code here that refers to variable fileref

for aline in olypmicsfile.readlines():
    values = aline.split(",")
    print(values[0], "is from", values[3], "and is on the roster for", values[4])

olypmicsfile.close()

# Better

olypmicsfile = open("/Users/wel51x/Box/MyBox/Courses/UMich/projects/IntroPython/data/olympics.txt", 'r')

for aline in olypmicsfile:
    values = aline.split(",")
    print(values[0], "is from", values[3], "and is on the roster for", values[4])

olypmicsfile.close()
