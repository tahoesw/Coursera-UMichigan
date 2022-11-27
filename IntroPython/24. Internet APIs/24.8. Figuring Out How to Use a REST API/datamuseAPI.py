# import statements for necessary Python modules
import requests

def get_rhymes(in_word, qty = 5):
    baseurl = "https://api.datamuse.com/words"
    params_diction = {}                     # Set up an empty dictionary for query parameters
    params_diction["rel_rhy"] = in_word     # rhyme with word passed in
    params_diction["max"] = str(qty)        # number of results
    resp = requests.get(baseurl, params=params_diction)
    # return the top three words
    word_ds = resp.json()
    #return [d['word'] for d in word_ds]    # return list of words
    return word_ds                          # Return a python object (list of dictionaries in this case)

items = zip(list(get_rhymes("funny")), list(get_rhymes("dash", 4)), list(get_rhymes("sauce")))
print("items that rhyme with funny, dash & sauce")
for item in items:
    print(item[0]['word'], item[0]['score'],
          '\t', item[1]['word'], item[1]['score'],
          '\t', item[2]['word'], item[2]['score'])
