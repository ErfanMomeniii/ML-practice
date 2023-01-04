name = input('What is your name\n')
print(name)

# type casting
num = int(input("Enter a number: "))
print(num, " ", type(num))

floatNum = float(input("Enter a decimal number: "))
print(floatNum, " ", type(floatNum))

# split with specific char
x = [int(x) for x in input("Enter multiple value: ").split(",")]
print("Number of list is: ", x)
