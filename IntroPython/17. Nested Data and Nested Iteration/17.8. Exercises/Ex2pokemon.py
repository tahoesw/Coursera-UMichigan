pokemon = {'Trainer1':
          {'normal': {'rattatas':15, 'eevees': 2, 'ditto':1}, 'water': {'magikarps':3}, 'flying': {'zubats':8, 'pidgey': 12}},
          'Trainer2':
          {'normal': {'rattatas':25, 'eevees': 1}, 'water': {'magikarps':7}, 'flying': {'zubats':3, 'pidgey': 15}},
          'Trainer3':
          {'normal': {'rattatas':10, 'eevees': 3, 'ditto':2}, 'water': {'magikarps':2}, 'flying': {'zubats':3, 'pidgey': 20}},
          'Trainer4':
          {'normal': {'rattatas':17, 'eevees': 1}, 'water': {'magikarps':9}, 'flying': {'zubats':12, 'pidgey': 14}}}
r = 0
d = 0
p = 0

print("-----------")
print(type(pokemon))
print(pokemon.keys())
print(pokemon.values())

for key, item in pokemon.items():
    print(key)
    print(type(key))
    print(item)
    print(type(item))
    if type(item) is dict:
        for ky, itm in item.items():
            print(ky)
            print(type(ky))
            print(itm)
            print(type(itm))
            if type(itm) is dict:
                for k, it in itm.items():
                    print(k)
                    print(type(k))
                    print(it)
                    print(type(it))
                    if (k == "rattatas"):
                        r += it
                    elif (k == "ditto"):
                        d += it
                    elif (k == "pidgey"):
                        p += it
print("totals for rattatas, dittos and pidgeys =", r, d, "and", p)
