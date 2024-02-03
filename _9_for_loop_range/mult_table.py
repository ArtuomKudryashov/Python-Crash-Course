# Определение размера таблицы
rows = 10
cols = 10

# Создание таблицы умножения
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        result = i * j
        print(f"{i} * {j} = {result}\t", end="")
    print()  # Переход на новую строку после каждой строки таблицы



for i in range(10):
    for j in range(10):
        print(j, end=" ")
    print()