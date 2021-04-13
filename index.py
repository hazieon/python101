print ("hello")
#type string
print (type (7))
#type integer
print (type (3 + 7j))
#simple addition - with 'j' being stand in number
#list (array) - mutable
my_list = ["taekwondo", "judo", "karate"]
#tuple - immutable
("dog", "cat", "horse")
#set - mutable, no duplicates
{"apple", "banana", "papaya"}

#dict (object) - mutable, key value pairs, not ordered
{"apples": 0, "papayas": 3, "plantains":7}

#methods:
my_list.insert (3, "aikido") 
my_list[0] = "jiujitsu"
print (my_list)
#demonstration of disallowed duplicates:
my_set = {"egg", "cheese", "milk", "egg"}

#duplicate item will only be printed once
print (my_set) 
my_dict = {"apples": 0, "papayas": 3, "plantains":7}

#update values, but not keys:
my_dict["apples"] = 3
print (my_dict)

#------------------------------------------

#Loops

fruits = ["apple", "papaya", "persimmon", "mango"]

#for loop:
for fruit in fruits:
    print(fruit)

#while loop: - need a 'counter' variable - i
i = 0

while fruits[i] != "papaya":
    print(fruits[i])
    
    i+=1
    
    
    
