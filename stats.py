def number_of_words():
    word_count = 0
    with open("/home/ruben_thomas/workspace/github.com/bootdotdev/curriculum/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    words = []
    words = file_contents.split()
    for word in words:
        word_count += 1
    return print(f"{word_count} words found in the document")

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
    return print(characters)


