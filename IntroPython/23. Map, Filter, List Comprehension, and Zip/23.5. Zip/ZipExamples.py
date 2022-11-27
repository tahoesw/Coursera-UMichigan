L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = []

for i in range(len(L1)):
    L3.append(L1[i] + L2[i])

print(L1)
print(L2)
print("L1 + L2:", L3)

print("---------")
# take multiple lists and turn them into a list of tuples using zip
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L4 = list(zip(L1, L2))
print(L1)
print(L2)
print("Paired using zip():", L4)

print("---------")

L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = []
L4 = list(zip(L1, L2))
# loop through the tuples
for (x1, x2) in L4:
    L3.append(x1+x2)

print(L4)
print("Sum tuples:", L3)

print("---------")

L1 = [3, 4, 5]
L2 = [1, 2, 3]
# using a list comprehension:
L3 = [x1 + x2 for (x1, x2) in list(zip(L1, L2))]
print(L3)

print("---------")

L1 = [3, 4, 5]
L2 = [1, 2, 3]
#using map and not unpacking the tuple
L3 = map(lambda x: x[0] + x[1], zip(L1, L2))
print(L3)
print(list(L3))

print("---------")

#two lists of numbers, L1 and L2. Using zip and list comprehension, create a new list, L3, that
# sums the two numbers if the number from L1 is greater than 10 and the number from L2 is less
# than 5. This can be accomplished in one line of code.
L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

L3 = [x1 + x2 for (x1, x2) in zip(L1, L2) if x1 > 10 and x2 < 5]
print("L1 =", L1)
print("L2 =", L2)
print("L1 + L2 where L1[i] > 10 and L2[i] < 5:", L3)