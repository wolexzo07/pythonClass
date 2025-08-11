inputONE = "I am a dev"
inputONE = "I am a  dev 4"
#print(inputONE)

"""
x = y = z = "Timothy Oluwole"
print(x)
print(y)
print(z)
"""

"""
x , y , z = "Oluwole" , "Timothy" ,"Biobaku"
print(x)
print(y)
print(z)

x = "oluwole"
y = "oluwole"
z = "oluwole"

def greet(name):
    return "Hi " + name + ", You are welcome"

print(greet("Ayodeji"))
print(greet("Timothy"))


def greet(name):
    print("Hi " + name + ", You are welcome")

greet("Ayodeji")
greet("Timothy")


def greet(name):
    #print("Hi " + name + ", You are welcome")
    return "Hi " + name + ", You are welcome"


names = ["Oluwole","timothy","Dada","Grace"]

for name in names:
    print(greet(name))
"""

names = ["Oluwole","timothy","Dada","Grace"]

#print(len(names))

#x = names.count("timothy")

#names.reverse()

#print(names)

"""
names.append("Peter")

print(names)

names.remove("timothy")

print(names)

names.pop(2)

print(names)
"""

#print(names.copy())

def greet(name , level):
    if(level == "1"):
        print("Hi " + name + ". You are a new recruit.")
    elif(level == "0"):
        print("Hi " + name + ". No admission yet.")
    elif(level == "2"):
        print("Hi " + name + ". You are the boss.")
    else:
        print("Hi " + name + " Sorry I can not place you ")

def sumUp(x , y , z):
    print(2*float(x)+4*float(y)+2*float(z))

greet("Biobaku Oluwole" , "2")
greet("Wale Oladeji" , "0")
greet("Fred Anderson" , "3")
greet("Ayodeji" , "1")


sumUp(2 , 3 , 4)
sumUp(4 , 23 , 1)
sumUp(6 , 9 , 2)
sumUp(2 , 31 , 3)