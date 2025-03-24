numbers = input("Введите вещественные числа через пробел: ").split()

with open("numbers.txt", "a") as file:
    for num in numbers:
        file.write(num + "\n")

print("Числа записаны в файл.")
