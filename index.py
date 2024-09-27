# 1. Write a Python program to calculate the length of a string.

string = "baqarzafarfarooqui"
print(len(string))


# 2. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'

string = "google.com"

dic = {}
for x in string :
    if x not in  dic:
        dic[x] = 1
    
    else:
        dic[x] += 1 

print(dic)

# 3. Write a Python program to get a string made of the first 2 and
# last 2 characters of a given string. If the string length is less than 2, 
# return the empty string instead.


string1 = "PakistanOne"


if len(string1)< 2:
    print(string1.replace(""))
else:
    print(string1)


 # member operator 


xyz = [10 , 20 , 40]

if 10 in xyz :
    print("yes we have this number")
    
#  identical operator 


x = 10 
y = 10 
z = 10 

print(x is y and x is z )




# control flow of  the  loop 

typerofgame = ["baqar" , "fatima" , "subhan" , "kashif"]


for x in typerofgame :
    if x == "subhan":
        continue
    else :
        print(x)




