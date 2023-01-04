# print(value(s), sep= ' ', end = '\n', file=file, flush=flush)
print("Hello", "World", sep='\n', end='', flush=False)

# write output in the file
print("Hello", "World", file=open("./output.txt", "w"))

# print with format
# %[flags][width][.precision]type
print("pi number is %1.5f " % 3.14)

# using format method
print("{} {} !".format("Hello", "World"))
print("{1} {0} !".format("Hello", "World"))
p = "Hello"
print(f"{p} World {'!'}")

# using string method
# string with "-" padding
print(p.center(10, '-'))
print(p.ljust(10, '-'))
print(p.rjust(10, '-'))
