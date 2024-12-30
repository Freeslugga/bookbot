from collections import Counter

def count_characters(book):
    book = book.lower()
    letters_only = ''.join(filter(str.isalpha, book))
    counts = Counter(letters_only)
    return counts

with open('books/frankenstein.txt') as f:
    file_contents = f.read()

char_counts = count_characters(file_contents)

print('--- Begin report of books/frankenstein.txt ---')
for char, count in char_counts.most_common():
    print(f'The {char} character was found {count} times')
print('--- End report of books/frankenstein.txt ---')
