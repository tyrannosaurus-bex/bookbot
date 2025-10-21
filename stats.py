def count_words(s):
    return len(s.split())

def count_char(text):
    char_dict = dict()
    for char in text:
        char_dict[char.lower()] = char_dict.get(char.lower(),0)+1
    return char_dict

def sort_on(items):
    return items["num"]

def sorted_list(char_dict):
    sorted_chars = list()
    for char, num in char_dict.items():
        sorted_chars.append({"char":char, "num":num})
        sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars

