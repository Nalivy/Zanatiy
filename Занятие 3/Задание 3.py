text = " какой-то текст"


text = text.replace(" ", "")


counts = {}
for char in text:
    counts[char] = counts.get(char, 0) + 1


sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)


top3 = sorted_counts[:3]


result = ", ".join([f"{char} – {count} раз" for char, count in top3])
print(result)
