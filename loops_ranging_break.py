# for loop 
name = "nishoth"
for letters in name:
    print(name)  

name = "nishoth"
for letters in name:
    print(letters)   

names = ["nishoth" , "nishan" , "karthik" , "john"]     
for name in names:
    print(names)

names = ["nishoth" , "nishan" , "karthik" , "john"]     
for name in names:
    print(name) 

for name in "hi i'm nishoth":
    print(name)    

names = ["nishoth" , "nishan" , "karthik" , "john"]     
for name in names:
    if name == "nishan":
        print("nishan is here")
    # else:
    #     print("nishan is not found") 
    # here we use the else condistion the output is 
        # nishan in not found
        # nishan is here
        # nishan ih not found
        # nishan is not found
names = ["nishoth" , "nishan" , "karthik" , "john"]     
for name in names:
    if name == "nishan":
        print("nishan is here")
        break
    else:
        print("nishan is not found") 

names = ["nishoth" , "nishan" , "karthik" , "john"]     
for name in names:
    if name == "nishan":
        print("nishan is here")
        continue
    else:
        print("nishan is not found") 

for i in range(5):
    print(i)

for i in range(5):
    print("nishoth")

for i in range(3,15):
    print(i)

for i in range(3,15,3):
    print(i)

for i in range(10):
    print(i)
    for j in range(2):
        print("nishoth" , j)
        for k in range(3):
            print("karthik" , k)

for i in range(0,100,2):
    print(i)

for i in range(1,100,2):
    print(i)