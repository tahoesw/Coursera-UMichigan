things = [2, 5, 9]

yourlist = [value * 2 for value in things]

print(things)
print("doubled:", yourlist)

print("---------")

def keep_evens(nums):
    new_list = [num for num in nums if num % 2 == 0]
    return new_list
lst = [3, 4, 6, 7, 0, 1]

print(lst)
print("Even numbers:", keep_evens(lst))

print("---------")

things = [3, 4, 6, 7, 0, 1]
print(things)
#chaining together filter and map:
# first, filter to keep only the even numbers
# double each of them
print("Keep evens, then double")
print("Using map and filter", list(map(lambda x: x*2, filter(lambda y: y % 2 == 0, things))))

# equivalent version using list comprehension
print("Using list comprehension", [x*2 for x in things if x % 2 == 0])

print("---------")

L = [12, 34, 21, 4, 6, 9, 42]
print(L)

print("Items > 10")
lst = []
for x in L:
    if x > 10:
        lst.append(x)
print("Using list iteration", lst)

# equivalent version using list comprehension
lst2 = [x for x in L if x > 10]
print("Using list comprehension", lst2)

print("---------")

print(L)

#Write code to assign to the variable compri all the values of the key name in any of the sub-dictionaries
# in the dictionary tester. Do this using a list comprehension.
tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
print(tester)

compri = [dictt['name'] for dictt in tester['info']]
print("List of names in dictionary:", compri)

result = [len(word) for word in compri if len(word) < 4]
print(result)
result = [word for word in compri if len(word) < 4]
print(result)
