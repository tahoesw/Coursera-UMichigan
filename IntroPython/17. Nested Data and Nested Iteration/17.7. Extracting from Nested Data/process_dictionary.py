import ast
import json

twitter_file = open("../../data/twitter_data_dict.txt", "r")
res = ast.literal_eval(twitter_file.read())

print("-----------")
print(type(res))
print(res.keys())

res2 = res['statuses']
print("----Level 2: a list of tweets-----")
print(type(res2)) # it's a list!
print(len(res2))  # looks like one item representing each of the three tweets
i = 1
for res3 in res2:
   print("\n----Level 3: tweet", i, "----")
   print(json.dumps(res3, indent=2)[:30])
   print(type(res3)) # it's a dictionary
   print(res3.keys())
   print(res3.values())
   res4 = res3['user']
   print("----Level 4: the user who wrote the tweet----")
#   print(type(res4)) # it's a dictionary
#   print(res4.keys())
   print(res4['screen_name'], res4['created_at'])
   i += 1

#succinct way
print("\n----Level 4: tweeters----")
for res3 in res['statuses']:
    print(res3['user']['screen_name'], res3['user']['created_at'])
