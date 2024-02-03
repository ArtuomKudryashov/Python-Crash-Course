fruits = ["apple", "banana", "cherry"]
print (fruits)

my_list = list
print(my_list)
print(len(fruits))

my_list1= [1,2,3]
my_list2= [1,3,2]
my_list=[1,2,3]
print(my_list1==my_list2)
print(my_list==my_list1)


print("banana" in  fruits)

fruit =fruits.pop()
print(fruit)
print(fruits)

fruits2=["fig","grape"]

fruits.extend(fruits2)
print(fruits)

fruits.sort(reverse=True)
print(fruits)
#
my_string = "My name is Artuom"
my_list  = my_string.split(" ")

print(my_list)

joined_string = " ".join(my_list)
print(joined_string)
my_list4= [1,3,4,5,6,3,3,2,4,4,5]
print(max(my_list4))
print(min(my_list4))
print(sum(my_list4))

word = 'hello'
word1= "Paython"

my_list= list(word)
print(my_list)

