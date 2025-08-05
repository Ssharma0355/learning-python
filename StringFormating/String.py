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

