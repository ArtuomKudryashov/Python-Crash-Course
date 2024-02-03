numbers_1 = [1,2,3,4,5]
numbers_2 = [6,7,8,9,10]

def find_average(numbers):
    average = sum (numbers)/len(numbers)
    return  average


average_1 = find_average(numbers_1)
average_2 = find_average(numbers_2)

print(average_1,  average_2)

def count_vowels(string):
    VOWELS = "AEOIUaeoui"
    count = 0
    for char in string:
        if char in VOWELS:
            count = count +1
            print(count)
            print(char)


count_vowels("qwrertyuireeee")
count_vowels("Yep")

def format_date(day: int , month: str):
    return f"The  date is {day} of {month}"

print(format_date(day=15, month= "October"))

def format_date2(*,day: int , month: str)->str:
    return f"The  date is {day} of {month}"

print(format_date2(day=15, month= "October"))


def customer_greeting(*, name: str, greeting: str = "Hello")->str:
    return f"{greeting}, {name}"

print(customer_greeting(name="Artuom", greeting= "Great day "))

print(customer_greeting(name="Nicki"))
