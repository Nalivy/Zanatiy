необходимые_экзамены = {
    "Информатика": 80,
    "Математика": 85,
    "Русский язык": 75
}

print("""Для определения возможности поступления, необходима информация о Вас.
Для ввода экзамена и баллов введите их через |: Химия | 40.
Для завершения ввода нажмите Enter.
""")

сданные_экзамены = {}

while True:
    ввод = input("").strip()
    if ввод == "":
        break
    try:
        экзамен, балл = [x.strip() for x in ввод.split("|")]
        сданные_экзамены[экзамен] = int(балл)
    except ValueError:
        print("Ошибка: введите экзамен и балл в формате 'Предмет | число'")
    except IndexError:
        print("Ошибка: в строке должен быть символ '|' между предметом и баллом")

print("Ваши экзамены:")
for i, (экзамен, балл) in enumerate(сданные_экзамены.items(), start=1):
    print(f"{i}) {экзамен} {балл}")

ok = True
for необходимый_экзамен, баллы in необходимые_экзамены.items():
    if необходимый_экзамен not in сданные_экзамены:
        print(f"Вы не сдавали {необходимый_экзамен}.")
        ok = False
        break
    if сданные_экзамены[необходимый_экзамен] < баллы:
        print(f"Недостаточно баллов по {необходимый_экзамен}.")
        ok = False
        break

print("Вы можете к нам поступить!" if ok else "Увы...")
