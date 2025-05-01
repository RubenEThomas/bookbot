

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

def sort(dict):
    return 

def end(characters,word_count): 
    list_of_characters = []
    for character in characters:
        if character.isalpha() == True:
            list_of_characters.append(character)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    list_of_characters.sort(key=None, reverse=False)
    for list_of_character in list_of_characters:
        print(f"{list_of_character} : {characters[list_of_character]}")
    print("============= END ===============") 
    print(characters)
    return
end(characters,word_count)