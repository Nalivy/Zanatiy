def ceasar(text, shift):
    letters = [chr(i) for i in range(ord('а'), ord('я') + 1)]
    result = ""
    for char in text:
        lower_char = char.lower()
        if lower_char in letters:
            index = letters.index(lower_char)
            new_index = (index + shift) % len(letters)
            new_char = letters[new_index]
            if char.isupper():
                result += new_char.upper()
            else:
                result += new_char
        else:
            result += char
    return result

try:
    text = input("Введите предложение: ")
    shift_input = input("Введите сдвиг: ")
    shift = int(shift_input)
    encoded = ceasar(text, shift)
    decoded = ceasar(encoded, -shift)
    print("Зашифрованная строка:", encoded)
    print("Расшифрованная строка:", decoded)
except ValueError:
    print("Ошибка: сдвиг должен быть числом!")
except Exception as e:
    print("Произошла другая ошибка:", e)
