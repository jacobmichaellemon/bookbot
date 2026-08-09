def get_num_words(words):
    words = words.split()
    num_words = len(words)
    return f"Found {num_words} total words"

def sort_on(items:tuple[str, int]) -> int:
    return items[1]

def chars_dict_to_sorted_list(toSort: dict[str, int]) -> list[tuple[str, int]]:
    new_list = []
    for key in toSort:
        new_list.append((key, toSort[key]))
    new_list = sorted(new_list, key=sort_on, reverse=True)
    return new_list

def sort_book_by_key(char_stats):
    list_of_stats = []
    for char in char_stats:
        temp_key = char
        temp_value = char_stats[char]
        entry = {"char" : temp_key , "count" : temp_value}
        list_of_stats.append(entry)
    list_of_stats.sort(reverse=True, key=sort_on)
    return list_of_stats

def get_chars_dict(text: str) -> dict[str, int]:
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


