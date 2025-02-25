import sys
from stats import get_num_words, get_book, get_num_per_characters, sorted_dictionary

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1) 

file_path = sys.argv[1] #"./books/frankenstein.txt"

book = get_book(file_path)
num_words = get_num_words(book)
dict_num_words = sorted_dictionary(get_num_per_characters(book))

print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(num_words)
print("--------- Character Count -------")

for dictionary in dict_num_words:

    letter = list(dictionary.keys())[0]
    if letter.isalpha():
        count = list(dictionary.values())[0]
        print(f"{letter}: {count}")

print("============= END ===============")