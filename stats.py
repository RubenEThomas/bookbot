import sys
def get_book_text(sys):
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    return 

def number_of_words(sys):
    word_count = 0
    words = []
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    words = file_contents
    for word in words:
        word_count += 1
    return word_count

word_count = number_of_words(sys)

def count_of_characters(sys):
    characters = {}
    with open(sys.argv[1]) as f:
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

characters = count_of_characters(sys)

def sort_on(dict):
    return dict["num"]

def new_dictionary(characters):
    sorted_list_of_dictionaries = []
    for character in characters:
        sorted_dict_of_characters = {"char": character, "num" : characters[character]}
        sorted_list_of_dictionaries.append(sorted_dict_of_characters)
    return sorted_list_of_dictionaries

sorted_list_of_dictionaries = new_dictionary(characters)

def end(sorted_list_of_dictionaries,word_count,sys): 
    sorted_list_of_dictionaries.sort(reverse = True, key = sort_on)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
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








