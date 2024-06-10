def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    words = text.split()
    word_count = len(words)
    print(word_count)
    # characters_count(text)
    print(characters_count(text.lower()))


def get_book_text(path):
    with open(path) as f:
        return f.read()


def characters_count(s):
    char_count = {}
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

main()