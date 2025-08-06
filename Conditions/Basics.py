# it gives in True or False 
x = 2
print(x == 2)
print(x == 3)
print(x != 2)
print(x < 2)

# Boolean operators 

# The "and" and "or" boolean operators allow building complex boolean expressions, for example:

name = "Sachin"
age = 23
if name == "Sachin" and age == 23:
    print("Hi ",name)

if name == "Sachin" or age == 24:
    print("Heyy", name)

if name == "Sachin" and age == 24:
    print("Heyy", name, "nice to meet you")


# The "in" operator
# The "in" operator could be used to check if a specified object exists within an iterable object container, such as a list:
    
name = "Modi"
if name in ["Gandhi","Modi"]:
    print("Your name is either Gandhi or Modi")