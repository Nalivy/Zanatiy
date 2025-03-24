vowels = "аеёиоуыэюя"

try:
    with open("poem.txt", "r", encoding="utf-8") as file:
        text = file.read()

    print("Стихотворение из файла:")
    print(text)

    words = text.split()
    vowel_count = 0
    consonant_count = 0

    for word in words:
        first_letter = word[0].lower()
        if first_letter.isalpha():
            if first_letter in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    print(f"Слов, начинающихся на гласную: {vowel_count}")
    print(f"Слов, начинающихся на согласную: {consonant_count}")

    if vowel_count > consonant_count:
        print("Больше слов на гласную.")
    elif consonant_count > vowel_count:
        print("Больше слов на согласную.")
    else:
        print("Гласных и согласных одинаково.")
except Exception as e:
    print("Ошибка при чтении стихотворения:", e)
