def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return print(file_contents)



from stats import end, number_of_words, count_of_characters
word_count = number_of_words()
characters = count_of_characters()
number_of_words()
count_of_characters()
end()
