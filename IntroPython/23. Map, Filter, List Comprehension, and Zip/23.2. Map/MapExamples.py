things = [2, 5, 9]

things4 = map((lambda value: 4*value), things)
print(list(things4))

# or all on one line
print(list(map((lambda value: 5*value), [1, 2, 3])))

print("---------")

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

print(lst)
greeting_doubled = map((lambda value: 2*value), lst)
print(greeting_doubled)
print(list(greeting_doubled))

print("---------")

abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]

print(abbrevs)
abbrevs_upper = map((lambda value: value.upper()), abbrevs)
print(abbrevs_upper)
print(list(abbrevs_upper))
