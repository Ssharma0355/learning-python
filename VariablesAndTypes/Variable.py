# Python is completely object oriented, and not "statically typed".
#  You do not need to declare variables before using them, or declare their type. 
# Every variable in Python is an object.

# Python supports two types of numbers - integers(whole numbers) and 
# floating point numbers(decimals). (It also supports complex numbers, 

myint = 7
print(myint)

myVar = 7.0

print(myVar)

# to make int into float 
myint = float(myint)
print(myint)

# Strings are defined either with a single quote or a double quotes.

myString = "Sachin"
print(myString)

my2ndString = 'Sharma'
print(my2ndString)

# The difference between the two is that using double quotes makes it easy to include apostrophes
#  (whereas these would terminate the string if using single quotes)

difference = "Sachin's macbook is easy to print"
print(difference)


# There are additional variations on defining strings that make it easier to include things such as carriage returns,
#  backslashes and Unicode characters. 
One = 1
Two = 2
sum = One + Two
print(sum)

Sachin = "Sachin"
Sharma = "Sharma"
Concat = Sachin + " " + Sharma
print(Concat)

# Assignments can be done on more than one variable "simultaneously" on the same line like this

(sachin, sharma) = ("Sachin", "Sharma")
print(sachin,sharma)

