def triple(value):
    return 3*value

def tripleStuff(a_list):
    new_seq = map(triple, a_list)
    return list(new_seq)

def quadrupleStuff(a_list):
    new_seq = map(lambda value: 4*value, a_list)
    return list(new_seq)

things = [2, 5, 9]
print("Original list:", things)
print("Tripled:", tripleStuff(things))
things4 = quadrupleStuff(things)
print("Quadrupled:", things4)
