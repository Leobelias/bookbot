import sys
from stats import number_of_words
from stats import number_of_characters
from stats import sorting_list

def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    wordcount = number_of_words(text)
    character_count = number_of_characters(text)
    sorted_list = sorting_list(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    print_report(sorted_list)
    print("============= END ===============")
    print(sys.argv)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(sorted_list):
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")


main()

