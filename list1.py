name=["nishoth","nishan","mithun","karthik","kiti","renu","thuva","john","dixon","abdul","jeno"]
print(len(name))
name.remove("nishan")
print(name)
name.append("nishanth")
print(name)
name[1]="nishan"
print(name)
name[10]="mithun"
print(name)
name.pop(1)
print(name)
name.pop()
print(name)
#sorting
name.sort()
print(name)
name.sort(reverse=True)
print(name)

# concatination
age=[22,25,36,26,28,50]
total=name+age
total.append(100)
print(total)


# tuple=(1,2,3,3,4,5,3,6)
# tuple.append("4")
# print(tuple)
tuple1=("nishoth","nishan")
print(tuple1[0].upper())
print(tuple1)

tuple=(1,2,3,3,4,5,3,6)
print(tuple.index(2))


tuple2=(1,5,3,8,9,4)
print(tuple+tuple2)


#repition
tuple3=(1,5,3,8,9,4)
print(tuple3*2)