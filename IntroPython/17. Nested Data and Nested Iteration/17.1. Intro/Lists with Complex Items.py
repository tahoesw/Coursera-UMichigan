nested1 = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
print(nested1[0])
print(len(nested1))
nested1.append(['i'])
print("-------")
for L in nested1:
    print(L)

print("\n========================")
nested1 = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
y = nested1[1]
print(y)
print(y[0])

print([10, 20, 30][1])
print(nested1[1][0])
print(nested1[2][1])
#blows up
#print(nested1[1][2])

print("\n========================")
def square(x):
    return x*x

L = [square, abs, lambda x: x+1]

print("****names****")
for f in L:
    print(f)

print("****call each of them****")
for f in L:
    print(f(-2))

print("****just the first one in the list****")
print(L[0])
print(L[0](3))

print("\n========================")

# to implement, needs to return index
def search_list(da_list, search_item):
    for item in da_list:
        if type(item) == str:
            if item == search_item:
                return item
        elif type(item) == int:
            if item == search_item:
                return item
    return None

data = ['bagel', 'cream cheese', 'breakfast', 'grits', 'eggs', 'bacon', [34, 9, 73, []],
        [['willow', 'birch', 'elm'], 'apple', 'peach', 'cherry']]
plant = ""
search_item = 73
i = 0
j = 0
k = 0
print("looking for", search_item)
print("in list:")
for item in data:
    print(i, item)
    if type(item) == str:
        if item == search_item:
            plant = item[i]
            print("item found at data[", i ,']')
    elif type(item) == int:
        if item == search_item:
            plant = item
            print("item found at data[", i, ']')
    elif type(item) == list:
        for itm in item:
            if type(itm) == str:
                if itm == search_item:
                    plant = itm
                    print("item found at data[", i ,'][', j,']')
            elif type(itm) == int:
                if itm == search_item:
                    plant = itm
                    print("item found at data[", i, '][', j, ']')
            elif type(itm) == list:
                # assume list of strings at this level
                for it in itm:
                    if it == search_item:
                        plant = it
                        print("item found at data[", i ,'][',j ,'][', k,']')
                    k += 1
                k = 0
            j += 1
        j = 0
    i += 1

# plant = data[7][0][0]
