'''For dictionaries, we have key and value pair.'''
my_dict={}
print(my_dict,type(my_dict))
my_dict1={'fruit':'apple','animal':'fox',1:'one','two':2}
print(my_dict1)
print(my_dict1['fruit'])
print(my_dict1.get('animal'))

'''Adding a new key value pair'''
my_dict1['three']=3
print(my_dict1)

'''Updating a value to a key'''
my_dict1['three']=59
print(my_dict1)

'''To get list of keys from dictionary'''
print(my_dict1.keys())
'''To get list of values from a dictionary'''
print(my_dict1.values())

'''To get key and value as one item'''
print(my_dict1.items())

'''Creating a new dictionary from keys'''
keys=['a','e','i']
new_dict=dict.fromkeys(keys)
print(new_dict)

#Set is an ordered list.
my_set={2,7,3,7,1}
print(my_set)
