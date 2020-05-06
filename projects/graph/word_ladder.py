f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()
print(words)

words_set = set()
for word in words:
    words_set.add(word)

