# how to get the user input
a = 10
b = 50
c = a + b 
print(c)
print(a+b)

name1 = (input("Enter your first name: "))
name2= (input("Enter your second name: "))
print(name1 + "_" + name2)

name1 = int(input("Enter your first number: "))  # int not accept the float value
name2= int(input("Enter your second number: "))
print(name1 + name2)

# float
name1 = float(input("Enter your first number: "))
name2= float(input("Enter your second number: "))
print(name1 + name2)

for i in range(10):
    a = int(input("Enter your number: "))
    print(i)

def add():
    a =int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(a+b)

add()