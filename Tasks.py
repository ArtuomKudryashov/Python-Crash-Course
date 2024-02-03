big_integer = 2**1000;
print(len(str(big_integer)))

my_string= "   Hello, world"
print ("ll" in my_string)
print(my_string.upper())

print(my_string.lower())
print(my_string.strip())

print(my_string.replace("lo","Python"))

print(my_string.count("o"))

print(my_string, str)
print((my_string.isdigit()))
# Проверка, состоит ли каждый символ строки из цифр
print(my_string.isdigit())

# Проверка, является ли переменная строкой
print(isinstance(my_string, str))

#Втавка  данных

name = "Artuom"

age= 39

print(f"Hello , my name  is {name} and  I'm {age} years old")

name = "Мир"
age = 25

formatted_string = "Привет, меня зовут %s и мне %d лет." % (name, age)

print(formatted_string)

