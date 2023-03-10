# Declaring a list
L = [1, "a", "string", 1 + 2]
print(L)

# Adding an element in the list at the end
L.append(6)
print(L)

# Appending element at the specific position
L.insert(1, "b")
print(L)

# Appending multiple elements to the list
L.extend([8, 10])
print(L)

# Deleting last element from a list
L.pop()
print(L)

# Removing element with specific value (if it doesn't exist throw error)
L.remove(3)
print(L)

# Displaying second element of the list
print(L[1])
