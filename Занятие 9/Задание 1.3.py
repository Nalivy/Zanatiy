numbers = []

try:
    with open("numbers.txt", "r") as file:
        for line in file:
            try:
                num = float(line.strip())
                numbers.append(num)
            except:
                continue

    if numbers:
        total = sum(numbers)
        maximum = max(numbers)

        with open("numbers.txt", "a") as file:
            file.write(f"Сумма (обновлённая): {total}\n")
            file.write(f"Максимум (обновлённый): {maximum}\n")

        print("Обновлённая сумма и максимум добавлены в файл.")
    else:
        print("В файле не найдено чисел.")
except Exception as e:
    print("Ошибка при чтении файла:", e)
