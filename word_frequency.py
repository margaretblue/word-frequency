#Write a program that looks for a file called sample.txt. contain the text of a book
# It reads this file and then returns the top 20 words used in the text
#and the number of times they are used.
# word_frequency()takes a string
#and returns a dictionary of all the words used in the string
#and the number of times they were used.
import re

def word_frequency(raw_string):
    #Todo: break string into list of lowered words with no punctuation
    word_string = (re.sub(r'[^A-Za-z]', " ", raw_string)).lower()
    #now break the string of words into a list separated by spaces
    word_list = word_string.split(" ")
    dict_of_all_words = {}

    for word in word_list:
        if word not in dict_of_all_words:
            dict_of_all_words[word] = 1
        else:
            dict_of_all_words[word] += 1
    #TODO replace below block with for loop of the chunk of banned words
    if dict_of_all_words['']:
        del dict_of_all_words['']

    return sorted(dict_of_all_words.items(), key=lambda x :x[1], reverse=True)

if __name__ == "__main__":
    print(word_frequency("There is a light And it Never goes out out. FAST light BEAR! "))
