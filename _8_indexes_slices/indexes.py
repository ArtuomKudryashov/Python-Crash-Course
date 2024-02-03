fruits=["apple", "banana" , "cherry", "watermelon"]
fruits[0] = "pineaplle"
print(fruits)


fruits[0],fruits[3]=fruits[3],fruits[0]
print(fruits)

fruits[1],fruits[3]=fruits[3],fruits[1]
print(fruits)

print( fruits[0:2])
listA = ( fruits[0:2])
print(listA)
print(fruits)
print(fruits[1:4:2])

# 3 ways reverse list
#1
numbers =[0,1,2,3,4,5,6,7,8,9,10]
print (numbers[::-1])

#2
numbers.reverse()
print (numbers)


#3
numbersNew= list(reversed(numbers))
print(numbersNew)

