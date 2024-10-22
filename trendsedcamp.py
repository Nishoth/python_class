name = "nishoth"
print(name)

print(name.count("h"))
print(len(name))
print(name.islower())
print(name.upper())

# we can change the data in list
# can't change the data in tuple
# can't allow the dupicated data in set

# function
def great(name):
    print(f'hello {name} welcome')
great('nishoth')

age=16
if age>18:
    print("you can vode")
else:
    print("you can't vode")

age=10
if age>18:
    print("your ticket price is 200rs")
elif age>6:
    print("your ticket price is 100rs")
else:
    print("you don't any dickets")

times = 6
while times > 0:
    print(times)
    times = times -1
