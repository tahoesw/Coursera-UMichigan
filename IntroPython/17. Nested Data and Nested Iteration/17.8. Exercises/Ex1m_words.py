# Iterate through the list so that if the character ‘m’ is in the string, then it should be
# added to a new list called m_list
d = ['good morning', 'hello', 'chair', 'python', ['music', 'flowers', 'facebook', 'instagram', 'snapchat', ['On my Own', 'monster', 'Words dont come so easily', 'lead me right']], 'Stressed Out', 'Pauver Coeur', 'Reach for Tomorrow', 'mariners song', 'Wonder sleeps here']

m_list = []
for item in d:
    #print(type(item))
    if type(item) is str:
        #print("string")
        if 'm' in item:
            #print(item)
            m_list.append(item)
    elif type(item) is list:
        for itm in item:
            #print(type(itm))
            if type(itm) is str:
                if 'm' in itm:
                    #print(itm)
                    m_list.append(itm)
            elif type(itm) is list:
                for it in itm:
                    #print(type(it))
                    if type(it) is str:
                        if 'm' in it:
                            #print(it)
                            m_list.append(it)
print(m_list)