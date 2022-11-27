import requests

# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
kval_pairs = {'rel_rhy': 'funny'}
page = requests.get("https://api.datamuse.com/words", params=kval_pairs)
print(page.url) # print the url that was fetched
print(page.text[:111])      # print the first 111 characters
print(page.text[112:232])   # print the next 120 characters
