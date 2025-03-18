def count_words(text):
    return len(text.split())

def count_character_appearances(text):
    appearances = {}
    for char in text:
        if char.lower() not in appearances:
            appearances[char.lower()] = 0
        appearances[char.lower()] += 1
    return appearances

def dict_parse(dict):
    parsed_dict = []
    for char in dict:
        parsed_dict.append({"char": char, "count": dict[char]})
    parsed_dict.sort(key=lambda x: x["count"], reverse=True)
    return parsed_dict
