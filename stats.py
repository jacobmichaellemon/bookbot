def get_num_words(words):
    words = words.split()
    num_words = len(words)
    return f"Found {num_words} total words"

def sort_on(items):
    return items["count"]

def sort_book_by_key(char_stats):
    list_of_stats = []
    for char in char_stats:
        temp_key = char
        temp_value = char_stats[char]
        entry = {"char" : temp_key , "count" : temp_value}
        list_of_stats.append(entry)
    list_of_stats.sort(reverse=True, key=sort_on)
    return list_of_stats

def book_char_stats(book):
    char_stats = {}

    for word in book:
        word = word.lower()
        for letter in word:
            if letter in char_stats:
                char_stats[letter] += 1
            else:
                char_stats[letter] = 1

    return char_stats

