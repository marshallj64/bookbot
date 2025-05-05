def get_word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    characters = {}
    for char in text.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_on(dict):
    return dict["num"]

def sort_characters(char_dict):
    sorted_list = []
    for char in char_dict:
        char_data = {"char": char, "num": char_dict[char]}
        sorted_list.append(char_data)

    sorted_list.sort(reverse=True, key=sort_on) 

    return sorted_list