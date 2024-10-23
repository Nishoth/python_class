# collection of multible data
employee_1 = {
    "name":"ramesh",
    "age":"25",
    "DOB":"24-07-1999"
}
employee_1["name"]="nishothnishan"  # update 
print(employee_1)
# {'name': 'ramesh', 'age': '25', 'DOB': '24-07-1999'}

employee_2 = {
    "name":"nishoth",
    "age":"26",
    "DOB":"24-07-1999"
}
employee_2["age"]=35
print(employee_2)
# {'name': 'nishoth', 'age': '26', 'DOB': '24-07-1999'}

employee_3 = {
    "name":"nishan",
    "age":"28",
    "DOB":"24-07-1999"
    # <key>      <dictionary>
}
print(employee_3.get("DOB"))
# 24-07-1999


my_dict = {
    "a":1,
    "b":2,
    "c":3,
    "d":4
}
print(my_dict)

# my_dict.clear()
print(my_dict)

# copy
x = my_dict.copy()
print(x)
# get
print(my_dict.get("c"))
# total key 
print(my_dict.keys())
# total value(data)
print(my_dict.values())
# delete
my_dict.pop("b")  
print(my_dict)

pop = my_dict.popitem()
print(pop)


x = my_dict.pop("c")
print(x)
print(my_dict)

po = my_dict.popitem()
print(po)
print(my_dict)

# update
other_dic = {
    "n":1,
    "i":2,
    "s":3,
    "h":4
}
my_dict.update(other_dic)
print(my_dict)

a = ("a","b","c","d")
b = (1,2,3,4)
c = dict(zip(a,b))
print(c)