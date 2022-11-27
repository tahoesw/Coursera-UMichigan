import json

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

a_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892},\n{"wrapperType":"other", "kind":"recording", "collectionId":1099}]}'
print(a_string)
d = json.loads(a_string)
print("------")
print(type(d))
print(d.keys())
print("resultCount = ",d['resultCount'])
# print(a_string['resultCount'])
# print("results = ",d['results'])
print("results = ")
items = d['results']
for item in items:
#    print(item.keys())
#    print(item.values())
    i = 0
    for key in list(item.keys()):
        print(key, '=', list(item.values())[i])
        i += 1

d = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2':{'b': 3, 'c': "yes"}}

print('--------')
print(d)
print(pretty(d))
