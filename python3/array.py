# array is useful when you want list of element with same type it handles that
# for example string in python is array of unicode characters
import array as arr

a = arr.array('i', [1, 2, 3])  # first argument shows type of array ('i'->int,'d'->double,'u'->unicode,'f'->float)
print(a)

# Appending element to the end of array
a.append(4)
print(a)

# Appending element at the specific position of array
a.insert(1, 5)
print(a)

# Removing element with value of array (if not exist throw error and
# if exist multiple element with that value it removes first of that)
a.remove(1)
print(a)

# Removing element with specific position from array
a.pop(2)  # if dont pass argument it removes last element from array
print(a)
