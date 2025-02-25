def get_book(file_path):

    with open(file_path) as f:
        book_text = f.read()

    return book_text

def get_num_words(file_path):

    book_text = get_book(file_path)
    num_words = len(book_text.split())

    return print(f"{num_words} words found in the document")

def get_num_characters(book_text):

    book_text = book_text.lower()

    dict_letters = {}

    for letter in book_text:
        if letter not in dict_letters:
            dict_letters[letter] = 0

        dict_letters[letter] += 1

    return dict_letters
