input("Enter your name:")
user_pin = "1234"
balance = "20 000rs"
pin = input("Enter your pin number:")
if user_pin == pin:
    print("pass")
    task = input('1 - widthrawel 2 - balance check 3 - deposit')
    if(task == '1'):
        print("widthrawel")
    elif(task=='2'):
            print("your balance is:",balance)
    elif(task == '3'):
        print("deposit")
    else:
        print("please check your input")
else:
    print("fail")
    
    