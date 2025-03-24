try:
    with open("numbers.txt", "r") as file:
        lines = file.readlines()

    numbers = [float(line.strip()) for line in lines]

    total = sum(numbers)
    maximum = max(numbers)

    with open("numbers.txt", "a") as file:
        file.write(f"Сумма: {total}\n")
        file.write(f"Максимум: {maximum}\n")

    print("Сумма и максимум добавлены в файл.")
except Exception as e:
    print("Не удалось прочитать файл. Ошибка:", e)
