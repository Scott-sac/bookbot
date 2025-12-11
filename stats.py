test = {"name1": 10,"name2": 11,"name3": 12}

def count_words(str_text):
    word_count = len(str_text.split())
    return word_count

def count_characters(str_text):
    dict_characters = {}
    words = str_text.split()
    letters = []
    for word in words:
        format_word = word.lower()
        for i in range(0, len(format_word)): # index of letter in format_word
            letters.append(format_word[i])

    for letter in letters:
        if letter in dict_characters:
            dict_characters[letter] += 1
        else:
            dict_characters[letter] = 1
    return dict_characters

def sort_on(input_dict): # helper for sorting on number of times the letter appears
    return input_dict["num"]

def list_dict(input_dict):
    list_dict = []
    for key in input_dict:
        if key.isalpha():
            list_dict.append({"letter": key, "num": input_dict.get(key)})
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict