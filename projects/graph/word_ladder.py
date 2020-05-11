from util import Queue

f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()
print(words)

words_set = set()
for word in words:
    words_set.add(word)

alphabet = ['a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

def get_neighbors(word):
    neighbors = []
    list_of_chars = list(word)
    for i in range(len(list_of_chars)):
        for letter in alphabet:
            new_word = list(list_of_chars)
            new_word[i] = letter
            new_word_string = "".join(new_word)
            if (new_word_string != word and new_word_string in words_set):
                neighbors.append(new_word_string)
    return neighbors

def find_path(begin_word, end_word):
    visited = set()
    words_to_visit = Queue()
    words_to_visit.enqueue([begin_word])
    while words_to_visit.size() > 0:
        path = words_to_visit.dequeue()
        current_word = path[-1]
        if current_word not in visited:
            visited.add(current_word)
            if current_word == end_word:
                return path
            for neighbor in get_neighbors(current_word):
                new_path = list(path)
                new_path.append(neighbor)
                words_to_visit.enqueue(new_path)

print(find_path('hit', 'cog'))
print(find_path('sail', 'boat'))