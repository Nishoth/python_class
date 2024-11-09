#  reuse the code 
def electrician():
    print("electrical work")
def painter():
    print("painting work")


electrician()
painter()

def phone():
    print("0764108354")

phone()
phone()
painter()

def addition():
    a = 10
    b = 20
    print(a+b)
addition()

def addition(a,b):
    print(a+b)

def subtraction(a,b):
    print(a-b)

addition(20,30)
subtraction(100,40)

def hi(name):
    print("Hi " + name + " welcome you")
user_name = input("Enter your name: ")
hi("user_name")

def hi(name):
    print("Hi " + name + " welcome you")

# Get user input
user_name = input("Enter your name: ")
hi(user_name)