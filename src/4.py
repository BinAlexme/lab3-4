words = input("Введите строку: ").lower().split()

seen = set()

for word in words:
    if word not in seen:
        result.append(f"{word}: {word_counts[word]}")
        seen.add(word)
