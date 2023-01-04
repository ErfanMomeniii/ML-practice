# Dictionary is like a map but key and value can have many different types
# on other hand I think it is a set that the value of that is pair of key and value
Dict = {0: '1', 2: 2}
print(Dict)

# Adding set of values
Dict['Value'] = {2, 3, "Hello"}
print(Dict)

# Updating existing Key's Value
Dict[2] = 'Welcome'
print(Dict)

# Adding Nested Key value to Dictionary
Dict[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
print(Dict)

# Accessing element using key
print(Dict['Value'])

# keys method returns keys from the dictionary
print(Dict.keys())

# values method returns values from the dictionary
print(Dict.values())

# pop method delete specific element by key
Dict.pop('Value')
print(Dict)

# Also like set it has an update method for adding many pairs to that
Dict.update({"1": 10, "a": 20})
print(Dict)
