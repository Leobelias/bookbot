def number_of_words(text):
    wordcount = text.split()
    return len(wordcount)

def number_of_characters(text):
    characters = {}
    lowercase_text = text.lower()

    for char in lowercase_text:
        if char in characters: 
            characters[char] +=1
        else:
            characters[char] =1
    return characters

def sorting_list(character_count):
    sorted_list = []
    for char, count in character_count.items():
        if char.isalpha(): 
            sorted_list.append({"char": char, "num": count})
    sorted_list.sort(key=num_count, reverse=True)
    return sorted_list
        


def num_count(item):
    return item["num"]
    


    return sorted_list