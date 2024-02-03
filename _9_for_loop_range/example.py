count =0
students = ["Ivan", "Bob" ,"Jack"]
for student in students:
    for char in student:
        if char == 'a':
            count =count+1
        print(char)

print("Total 'a' count:", count)