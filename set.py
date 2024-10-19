# tuple la erukkiratha cut pannina = set
# collection of multiple data
# mentioned in curly braces{}
# sets not allow duplicate elements
# it has no fixed index value

my_set = {"apple","orange","mango","apple"}
print(my_set)
# it's can't accept the duplicated values
# using gaming , user id like duplicate not accepted

# adding elements
my_set.add("panana")
print(my_set)

my_set.update(["kiwi","watermalon"])
print(my_set)

my_set.remove("apple")
print(my_set)

my_set.clear()
print(my_set)

# 
my_set1={"apple","orange","mango"}
my_set2={"kiwi","watermelon","pineapple","apple"}
my_set3=my_set1.union(my_set2)
print(my_set3)


# common a erukkirathu
my_set1={"apple","orange","mango"}
my_set2={"kiwi","watermelon","pineapple","apple"}
my_set3=my_set1.intersection(my_set2)
print(my_set3)

my_set1={"apple","orange","mango"}
my_set2={"kiwi","watermelon","pineapple","apple"}
my_set3=my_set1.difference(my_set2)
print(my_set3)
