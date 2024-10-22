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

b = my_dict.copy()
print(b)

print(my_dict.keys())

print(my_dict.values())

my_dict.pop("b")  # delete
print(my_dict)

b = my_dict.pop("b") 
