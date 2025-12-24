import sys
from stats import get_num_words, get_num_chars, dict_to_sorted_list

def get_book_text(file_path: str):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    book_text = get_book_text(path)
    word_count = get_num_words(book_text)
    char_count = get_num_chars(book_text)
    sorted_char_count = dict_to_sorted_list(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char in sorted_char_count:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['count']}")

main()

