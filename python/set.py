# set is unordered and all values in that are unique
s1 = {"hello", 2}  # or set(["hello",2])

# add element
s1.add(3)
print(s1)

# add duplicate value
s1.add(3)
print(s1)

# add many values with update
s1.update([1, 4])
print(s1)

# The difference between discard and remove is in remove if the key doesn't found it returned an error
# but in discard, it only changed nothing
s1.discard(1)
s1.remove(2)
print(s1)

# pop method delete first element
s1.pop()
print(s1)

# clear method delete all elements
s1.clear()
print(s1)

# union returned the union of sets in the new set
s1 = {1}
s1.union({1, 2, 3})
print(s1)
