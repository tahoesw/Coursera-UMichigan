#import json
import requests
from requests_html import HTMLSession

parameters = {"q": "violins and guitars", "tbm": "isch"}
results = requests.get("https://google.com/search", params = parameters)

#print(results.url)
#print(results.text)

#jsonPage = results.json()
#print(jsonPage[0])

print("Requested url:", results.url, "\n\nUsing requests")            # print the url that was fetched
keys = list(results.headers.keys())
values = list(results.headers.values())
print("Headers:")
i = 0
for _ in keys:
    print("  ", keys[i],":", values[i])
    i += 1

print(results.text[:122])

#keys = list(results.body.keys())
#values = list(results.body.values())
#return an iterator, one item for each line:
print(results.iter_lines())

#looping through the iterator:
#for c in results.iter_lines():
#  print(c)

#html

session = HTMLSession()

r = session.get("https://google.com/search", params = parameters)

links = r.html.links
print("\nUsing HTMLSession\n",type(links))
print("Links containing images")
for link in links:
    if "image" in link and "search" not in link:
        print(link)