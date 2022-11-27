# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Winston\n')

# Dictionary exercise 1
sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
word_counts = {}
for word in sentence.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print(word_counts)

# Dictionary exercise 2
placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."

d = {} # start with an empty dictionary
for c in placement:
    if c not in d:
        # we have not seen this character before, so initialize a counter for it
        d[c] = 0

    #whether we've seen it before or not, increment its counter
    d[c] = d[c] + 1

ks = d.keys()

min_value = list(ks)[0]
max_value = list(ks)[0]

for k in ks:
    if d[k] < d[min_value]:
        min_value = k
    if d[k] > d[max_value]:
        max_value = k

print("\nDict entry with lowest count:", min_value, d[min_value])
print("Dict entry with highest count:", max_value, d[max_value])
if max_value == ' ':
    print("highest count char is a blank")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print()
da = {'key1': {'a': 5, 'c': 90, 5: 50}, 'key2':{'b': 3, 'c': "yes"}}
print(da)
da[5] = {1: 2, 3: 4}
print(da)
da = {'key1': {'a': 5, 'c': 90, 5: 50}, 'key2':{'b': 3, 'c': "yes"}}
print(da)
da['key1']['d'] = da['key2']
print(da)
da = {'key1': {'a': 5, 'c': 90, 5: 50}, 'key2':{'b': 3, 'c': "yes"}}
print(da)
da['key2'] = 3
print(da)

def distance(x1, y1, x2, y2):
    ret = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5
    return ret

print(distance(1,2, 1,2))
assert distance(1,2, 1,2) == 0
assert distance(1,2, 4,6) == 5
print(distance(0,0, 1,1))
assert distance(0,0, 1,1) == 2**0.5
