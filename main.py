import sys
from stats import get_num_words, get_chars_dict, sort_book_by_key, chars_dict_to_sorted_list

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
        if stat[0].isalpha():
            print(f"{stat}")

    print("============= END ===============")
    return 0


def main():
    book_path = None
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
    else:
        print("Expected usage main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text(book_path)
    num_words = get_num_words(book)
    stats = get_chars_dict(book)
    #sorted_stats = sort_book_by_key(stats)
    print_sorted_report(num_words, chars_dict_to_sorted_list(stats), book_path)

main()