try:
    n = int(input("Введите кол-во человек: "))
    middle_names = {}
    count = 0
    for i in range(n):
        fio = input("Введите ФИО через пробел: ").split()
        if len(fio) < 3:
            continue
        middle_name = fio[2]
        middle_names[middle_name] = middle_names.get(middle_name, 0) + 1
        count += 1
    if middle_names:
        most_common = sorted(middle_names.items(), key=lambda item: item[1])[-1][0]
        print("Самое частое отчество:", most_common)
    else:
        print("Ни у кого не было отчества.")
    print("В расчете участвовало человек:", count)
except ValueError:
    print("Ошибка: введите число.")
except Exception as e:
    print("Произошла ошибка:", e)
