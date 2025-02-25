def get_book(file_path):

    with open(file_path) as f:
        book_text = f.read()

    return book_text

def get_num_words(book_text):
    num_words = len(book_text.split())
    return f"Found {num_words} total words"

def get_num_per_characters(book_text):

    book_text = book_text.lower()
    dict_letters = {}

    for letter in book_text:
        if letter not in dict_letters:
            dict_letters[letter] = 0
        dict_letters[letter] += 1

    return dict_letters

def sorted_dictionary(dict_letters):
    lst_dict = []

    for key in dict_letters:
        temp_dict = {}
        temp_dict[key] = dict_letters[key]
        lst_dict.append(temp_dict)

    def sort_on(dict_item):
        return list(dict_item.values())[0]

    lst_dict.sort(key=sort_on, reverse=True)

    return lst_dict