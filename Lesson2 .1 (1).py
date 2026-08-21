
  
#Data types

myString="Rajeeve"  #Variable holds a string data type
myNumber= 10        #Variable holds a number data type
myFloat=10.1        #Variable holds a decimal data type
isAddress=True      #Variable holds a boolean data type

print (myString)
print (myNumber)
print (myFloat)
print (isAddress)

myFullName=myString +" Abraham"
print("my full name is " + myFullName)

age=input("What is your age")
print(age)

address=input("Emter your addrwss")
print(address) 


#Structures

print ("LISTS")
#List - Allows to add duplicates and can add and remove items

myList =["apple","banana","milk"]
print  (myList)

myDuplicateList =["apple","banana","milk","apple"] # duplicated apple
print  (myDuplicateList)

myList.append("Sugar")  #added sugar to the list
print  (myList)

myList.remove("milk") #Removed milk from the list 
print  (myList)

for x in myList: #Loop through myList
  print x

print("\n")
#Tuples - tuples are ordered ,unchangable and cant remove items
print ("TUPLES")
myTuple=("Lady","boys","Girls")
print (myTuple)

print("\n")
#Tuples - sets are unordered ,unchangable and unindexed items

print ("SETS")

mySet={"apple","banana","milk"}
print(mySet)

#Dictinory - Dictionary  are used to store key value pairs

print ("DICTIONARY")
myDictionary={"Name":"Rajeeve",
              "Surname":"Abraham",
              "Course"  :"AI and Python programming"}

print (myDictionary)

print("\n")
