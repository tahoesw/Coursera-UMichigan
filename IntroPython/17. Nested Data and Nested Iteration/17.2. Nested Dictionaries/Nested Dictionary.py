info = {'personal_data':
         {'name': 'Lauren',
          'age': 20,
          'major': 'Information Science',
          'physical_features':
             {'color': {'eye': 'blue',
                        'hair': 'brown'},
              'height': "5'8"}
         },
       'other':
         {'favorite_colors': ['purple', 'green', 'blue'],
          'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
         }
      }

print(info)
for v in info.values():
    print(v)
    if type(v) == dict:
        l = 0
        print(v.keys())
        for v1 in v.values():
            if list(v.keys())[l] == "color":
                color = v1
            print("key =", list(v.keys())[l])
            print(v1)
            l += 1
            if type(v1) == dict:
                m = 0
                print(v1.keys())
                for v2 in v1.values():
                    if list(v1.keys())[m] == "color":
                        color = v2
                    print("key =", list(v1.keys())[m])
                    print(v2)
                    m += 1
                    if type(v2) == dict:
                        n = 0
                        print(v2.keys())
                        for v3 in v2.values():
                            if list(v2.keys())[n] == "color":
                                color = v3
                            print("key =", list(v2.keys())[n])
                            print(v3)
                            n += 1
print(color)

#submitted code
for v in info.values():
    if type(v) == dict:
        l = 0
        for v1 in v.values():
            if list(v.keys())[l] == "color":
                color = v1
                break
            l += 1
            if type(v1) == dict:
                m = 0
                for v2 in v1.values():
                    if list(v1.keys())[m] == "color":
                        color = v2
                        break
                    m += 1
                    if type(v2) == dict:
                        n = 0
                        for v3 in v2.values():
                            if list(v2.keys())[n] == "color":
                                color = v3
                                break
                            n += 1
print("Color is/colors are:", color)
