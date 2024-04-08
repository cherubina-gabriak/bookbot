def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_words_count(text)
    chars_dict = get_letters_count(text)
    sorted_chars = chars_dict_to_sorted_list(chars_dict)

    print_report(book_path, word_count, sorted_chars)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words_count(text):
    return len(text.split())

def get_letters_count(text):
    chars = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char in chars:
            chars[lowered_char] += 1
        else:
            chars[lowered_char] = 1

    return chars

def sort_on(dict):
    return dict["count"]

def chars_dict_to_sorted_list(chars):
    sorted_list = []

    for char in chars: 
        sorted_list.append(
            {"name": char, "count": chars[char]}
        )

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def print_report(path, words_count, list):
    print(f"--- Begin report of {path} ---")
    print(f"{words_count} words found in the document")
    print()

    for char in list:
        if not char["name"].isalpha():
            continue

        print(f"The '{char["name"]}' charachter was found {char["count"]} times")

    print()
    print("--- End report ---")

main()
