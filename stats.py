

def number_of_words():
    word_count = 0
    with open("/home/ruben_thomas/workspace/github.com/bootdotdev/curriculum/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    words = []
    words = file_contents.split()
    for word in words:
        word_count += 1
    return word_count

word_count = number_of_words()

def count_of_characters():
    characters = {}
    with open("/home/ruben_thomas/workspace/github.com/bootdotdev/curriculum/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        words = []
        words = file_contents.split()
    for word in words:
        word = word.lower()
        letters = list(word)
        for letter in letters:
            if letter in characters:
                characters[letter] += 1
            else:
                characters[letter] = 1
    return characters

characters = count_of_characters()

def sort_on(dict):
    return dict["num"]

def new_dictionary(characters):
    sorted_list_of_dictionaries = []
    for character in characters:
        sorted_dict_of_characters = {"char": character, "num" : characters[character]}
        sorted_list_of_dictionaries.append(sorted_dict_of_characters)
    return sorted_list_of_dictionaries

sorted_list_of_dictionaries = new_dictionary(characters)

def end(sorted_list_of_dictionaries,word_count): 
    sorted_list_of_dictionaries.sort(reverse = True, key = sort_on)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for sorted_list_of_dictionarie in sorted_list_of_dictionaries:
        if sorted_list_of_dictionarie["char"].isalpha():
            print(f"{sorted_list_of_dictionarie["char"]}: {sorted_list_of_dictionarie["num"]}")

    print("============= END ===============") 
    return



def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return print(file_contents)








