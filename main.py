import sys
from stats import get_num_words, char_count, chars_descending


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    content = get_book_text(file_path)
    num_words = get_num_words(content)
    num_chars = char_count(content)
    chars_order = chars_descending(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for val in chars_order:
        key = val['char']
        val = val['num']
        if key.isalpha():
            print(f"{key}: {val}")
    print("============= END ===============")


main()
