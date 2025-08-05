# Python uses C-style string formatting to create new, formatted strings. 
# The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), 
# together with a format string, which contains normal text together with "argument specifiers",
#  special symbols like "%s" and "%d".

name = "Sachin"
age =24
print("%s is %d years old"%(name, age))

# Any object which is not a string can be formatted using the %s operator as well. 
# The string which returns from the "repr" method of that object is formatted as the string. For example:

myList = [1,2,3]
print("The list is %s" % myList)

# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

myData = ("Sachin", "Sharma", 24)
formatString = "Hello %s %s. Your age is %s."
print(formatString % myData)