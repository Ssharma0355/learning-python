# types of strings
str1 = 'single quote'
str2 = "double quote"
str3 = '''triple quote'''

print(str1,str2,str3)

# and for next line and giveing tab space we use escape sequaence 

spaceSeq = "My name is Sachin's \nand i am a python developer \tmy domain is SDE"
print(spaceSeq)


# Concatination of String 

strName = "Sachin"
strSurname = "Sharma"
name = strName + strSurname
print(name)
# show length of an string variable 
print(len(name))

# indexing 
nameForIndex = "Sachin"
print(nameForIndex[2])
# shows c 

# Sliceing 
# accessing parts of string 

NormalString = "Machince Learning"
print(NormalString[1:5])
print(NormalString[1:len(NormalString)])
print(NormalString[:len(NormalString)])
print(NormalString[:])


# prints -> achi

# -ve slicing 

negStr = "Sachin"
#    -5,-4,-3,-2,-1
print(negStr[-3:-1])
# o/p - > hi
print(negStr.endswith("in"))
# o/p-> True 
capsName = "saChin"
print(capsName.capitalize())

print(capsName.replace("C","O"))
# Sachin -> saOhin
