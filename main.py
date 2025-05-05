import sys 

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
from stats import end, number_of_words, count_of_characters, new_dictionary
word_count = number_of_words(sys)
characters = count_of_characters(sys)
sorted_list_of_dictionaries = new_dictionary(characters)
end(sorted_list_of_dictionaries, word_count,sys)
