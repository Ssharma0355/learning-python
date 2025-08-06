string = "Sachin"
print(string[::-1])

# reverse a string like this

print(string.upper())
print(string.lower())

# for upper case and lower case for string 

array = [1,2,3,4,5]
print(array[::-1])

# reverse an array 


sampleString = "Sachin GOAT"
print(sampleString.startswith("Sachin")) 
# it checks if the string starts with the same string  
print(sampleString.endswith("Bakri"))
#  it checks if the string ends with the same string 



# This splits the string into a bunch of strings grouped together in a list.
#  Since this example splits at a space, the first item in the list will be "Hello", and the second will be "world!".

astring = "Hello world!"
afewwords = astring.split(" ")
print(afewwords)
# o/p -> ['Hello', 'world!'] 

aString = "Sachin is a good guy for development"
makingList = aString.split(" ")
print(makingList) 
# o/p -> ['Sachin', 'is', 'a', 'good', 'guy', 'for', 'development']
print(makingList[3])
# o/p-> good 
