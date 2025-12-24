from typing import Union

def get_num_words(text: str):
    words = text.split()
    return len(words)

def get_num_chars(text: str) -> dict[str, int]:
    chars_dict: dict[str, int] = {}

    for char in text:
        lower_case_char = char.lower()
        if lower_case_char in chars_dict:
            chars_dict[lower_case_char] += 1
        else:
            chars_dict[lower_case_char] = 1

    return chars_dict

def sort_on(l):
    return l["count"]

def dict_to_sorted_list(d: dict[str, int]):
    list_of_dicts = []

    for item in d:
        list_of_dicts.append({"char": item, "count": d[item]})

    list_of_dicts.sort(reverse=True, key=sort_on)

    return list_of_dicts
