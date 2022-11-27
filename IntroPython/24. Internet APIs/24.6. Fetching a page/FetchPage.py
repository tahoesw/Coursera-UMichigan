import requests
import json

page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
print(type(page))
print(page.text[:150])                      # print the first 150 characters
print("Requested url:", page.url)            # print the url that was fetched
keys = list(page.headers.keys())
values = list(page.headers.values())
print("Headers:")
i = 0
for _ in keys:
    print("  ", keys[i],":", values[i])
    i += 1
print("------")
jsonPage = page.json()                      # turn page.text into a python object
print("jsonPage is:", type(jsonPage))
print("---first item in the list---")
print(jsonPage[0])
print("---the whole list, pretty printed---")
print(json.dumps(jsonPage, indent=2))       # pretty print the results
