import sys
from stats import get_num_words, book_char_stats, sort_book_by_key

def get_book_text(filepath):
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_sorted_report(num_words, sorted_stats, book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")        
    print(num_words)
    print("--------- Character Count -------")

    for stat in sorted_stats:
        temp_char = stat["char"]
        temp_count = stat["count"]
        if temp_char.isalpha():
            print(f"{temp_char}: {temp_count}")

    print("============= END ===============")
    return 0


def main():
    book_path = None
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text(book_path)
    num_words = get_num_words(book)
    stats = book_char_stats(book)
    sorted_stats = sort_book_by_key(stats)
    print_sorted_report(num_words, sorted_stats, book_path)

main()