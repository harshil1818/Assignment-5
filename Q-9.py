from collections import Counter
words = input("enter the list of words (space-separated):").split()

word_count = Counter(words)

print("word_count:")

for word, count in word_count.items():
    print(f"{word}: {count}")