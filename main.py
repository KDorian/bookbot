def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    words = text.split()
    word_count = len(words)
    # print(word_count)
    # characters_count(text)
    characters_array = characters_count(text.lower())
    # print(characters_array)
    sorted_char_count = sort_dict_by_values_then_keys(characters_array)
    # print(sorted_char_count)

    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{word_count} words found in the document')
    print()
    print_dictionary(sorted_char_count)
    print('--- End report ---')


def get_book_text(path):
    with open(path) as f:
        return f.read()


def characters_count(s):
    char_count = {}
    
    for char in s:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    return char_count

def sort_dict_by_values_then_keys(d):
    return dict(sorted(d.items(), key=lambda item: (-item[1], item[0])))

def print_dictionary(d):
    for key, value in d.items():
        print(f"The '{key}' character was found {value} times")

main()