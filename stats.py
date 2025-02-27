def get_num_words(text):
    return len(text.split())

def get_frequency(text):
    frequency = {}
    text = text.lower()
    for char in text:
        if char not in frequency:
            frequency[char] = 1
        else:
            frequency[char] += 1
    return frequency

def sort_on(dictionary):
    return dictionary["freq"]

def get_dict(dictionary):
    dict_list = []
    for key in dictionary:
        if key.isalpha():
            dict_list.append({"char": key, "freq": dictionary[key]})
    dict_list.sort(key=sort_on, reverse=True)
    return dict_list