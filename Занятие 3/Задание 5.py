text = "пример строки"
letter = "с"

if letter in text:
    first_index = text.find(letter)
    last_index = text.rfind(letter)
    print("Первый индекс:", first_index)
    print("Последний индекс:", last_index)
else:
    print("Буквы нет в строке")
