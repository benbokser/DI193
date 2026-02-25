# Daily challenge : Text Analysis
# Last Updated: November 5th, 2025
# Instructions:

# Create a Text class to analyze text data, either from a string or a file. Then, create a TextModification class to perform text cleaning.


# Part I: Analyzing a Simple String
# Step 1: Create the Text Class

#     Create a class called Text.
#     The __init__ method should take a string as an argument and store it in an attribute (e.g: self.text).
import re
import string

class Text:
    def __init__(self, text):
        self.text = text


# Step 2: Implement word_frequency Method
#     Create a method called word_frequency(word).
#     Split the text attribute into a list of words.
#     Count the occurrences of the given word in the list.
#     Return the count.
#     If the word is not found, return None or a meaningful message.
    def word_frequency(self, word):
        word_list = self.text.split()
        word_count = word_list.count(word)
        if word_count == 0:
            return None
        return word_count

# Step 3: Implement most_common_word Method
#     Create a method called most_common_word().
#     Split the text into a list of words.
#     Use a dictionary to store word frequencies.
#     Find the word with the highest frequency.
#     Return the most common word.
    def most_common_word(self):
        word_list = self.text.split()
        word_dict = {}
        for word in word_list:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
        most_common = max(word_dict, key=word_dict.get)
        return most_common


# Step 4: Implement unique_words Method

#     Create a method called unique_words().
#     Split the text into a list of words.
#     Use a set to store unique words.
#     Return the unique words as a list.

    def unique_words(self):
        word_list = self.text.split()
        word_set = set(word_list)
        return list(word_set)

# Part II: Analyzing Text from a File

# Step 5: Implement from_file Class Method

#     Create a class method called from_file(file_path).
#     Open the file at file_path in read mode.
#     Read the file content.
#     Create and return a Text instance with the file content as the text.
    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r") as f:
            content = f.read()
            return cls(content)



# Bonus: Text Modification

# Step 6: Create the TextModification Class

#     Create a class called TextModification that inherits from Text.
class TextModification(Text):


# Step 7: Implement remove_punctuation Method

#     Create a method called remove_punctuation().
#     Use the string module to get a string of punctuation characters.
#     Use a string method or regular expressions to remove punctuation from the text attribute.
#     Return the modified text.
    def remove_punctuation(self):
        punctuation = string.punctuation
        return self.content.translate(str.maketrans('', '', punctuation))


# Step 8: Implement remove_stop_words Method

#     Create a method called remove_stop_words().
#     Search online for a list of English stop words (common words like “a”, “the”, “is”).
#     Split the text into a list of words.
#     Filter out stop words from the list.
#     Join the remaining words back into a string.
#     Return the modified text.
    def remove_stop_words(self):
        with open('stopwords-en.txt', "r") as f:
            stopwords_str = f.read()
            stop_set = set(stopwords_str.split())
        self_list = self.text.split()
        filtered = [word for word in self_list if word not in stop_set]
        filtered_str = ' '.join(filtered)
        return filtered_str



# Step 9: Implement remove_special_characters Method

#     Create a method called remove_special_characters().
#     Use regular expressions to remove special characters from the text attribute.
#     Return the modified text.
    def remove_special_characters(self):
        return re.sub(r'[^a-zA-Z0-9\s]', '', self.text)

