from collections.abc import Hashable

info = {}
info["фио"] = "Зюзин Богдан Юрьевич"
info["дата_рождения"] = "25/07/2005"
info["место_рождения"] = "Липецк"

print(info)

info["хобби"] = ["чтение", "рисование"]
info["хобби"].append("программирование")

info["животное"] = ("кот Жора")

info["ЕГЭ"] = {}
info["ЕГЭ"]["Русский язык"] = 85
info["ЕГЭ"]["Математика"] = 90
info["ЕГЭ"]["Информатика"] = 78
info["ЕГЭ"]["Химия"] = 40
del info["ЕГЭ"]["Химия"]

info["вузы"] = {}
info["вузы"]["ВГУ"] = 290
info["вузы"]["ВГУИТ"] = 260
info["вузы"]["ВГТУ"] = 240

print("Данные:")
print(info)

exams = sorted(info["ЕГЭ"].keys())
print("Предметы:", ", ".join(exams))

uni = sorted(info["вузы"].keys())
print("Вузы:", ", ".join(uni))

print("\nОтветы на вопросы:")

name = info["фио"].split()[1]
starts_with_vowel = name[0].lower() in "аеёиоуыэюя"
print("* мое имя начинается на гласную букву:", starts_with_vowel)

month = int(info["дата_рождения"].split("/")[1])
born_in_winter_or_summer = month in (12, 1, 2, 6, 7, 8)
print("* родился летом или зимой:", born_in_winter_or_summer)

hobbies_count = len(info["хобби"])
print("* у меня {} хобби, первое \"{}\"".format(hobbies_count, info["хобби"][0]))

print("* после окончания школы сдавал {} экз.".format(len(info["ЕГЭ"])))

sum_mark = sum(info["ЕГЭ"].values())
print("* сумма баллов = {}".format(sum_mark))

max_mark = max(info["ЕГЭ"].values())
print("* макс. балл = {}".format(max_mark))

vuz_count = sum(int(sum_mark >= score) for score in info["вузы"].values())
print("* кол-во вузов в которые прохожу: {}".format(vuz_count))
