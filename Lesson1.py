# print("Hello","world",sep=" $$ " , end = " Artuom")
# name = input ("Enter your name: ")
# print(name)
# name, age = "Artuom",  39
# print(name,  age)
#
# a= 10;
# b= 15;
#
# a,b = b,a;
# #Свопинг
# print(a,b)
# #type
# print(type(a))

flat_number =24
entrance_number = (flat_number-1)//20+1
print(entrance_number)




floor_number = (flat_number-1)%20//4+1
print(floor_number)
x= 6
print( x< 10 and x>-8)
print( x< 10 or x>100)
num =10
if num == 101:
    print("Hip-Hop")
else:
    print("Not hip-hop")

age = 2004

if ((age % 4==0 and age % 100 !=0 ) or age  % 400 ==0 ):
    print("Year is leap")
else:
    print("Year is not leap")

str= str(age)

lenght = len(str)

print(lenght)

print(type(str))

my_int = int(str)
print(type(my_int))
print(my_int)