from stats import get_num_words, get_book, get_num_characters

file_path = "./books/frankenstein.txt"

book = get_book(file_path)

dict_num_words = get_num_characters(book)

print(dict_num_words)