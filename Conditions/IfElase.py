x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

# The 'is' operator
# Unlike the double equals operator "==", the "is" operator does not match the values of the variables,
    #  but the instances themselves. For example:

x = [1,2,3]
y = [1,2,3]
print(x == y) 
# True
print(x is y)
# False

