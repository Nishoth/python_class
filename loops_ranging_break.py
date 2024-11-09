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