dictionary = {'language': 'python', 'version': '3.8', 'app':None, 'ide': None}
dict1={i:dictionary[i] for i in dictionary if dictionary[i] is not None}
print(dict1)