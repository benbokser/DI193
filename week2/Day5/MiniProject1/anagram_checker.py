# Create a new file called anagram_checker.py which contains a class called AnagramChecker.

# The class should have the following methods:

#     __init__ - should load the word list file (text file) into a variable, so that it can be searched later on in the code.
#     is_valid_word(word) – should check if the given word (ie. the word of the user) is a valid word.

#     get_anagrams(word) – should find all anagrams for the given word. (eg. if word of the user is ‘meat’, the function should return a list containing [“mate”, “tame”, “team”].)

#     Hint: you might want to create a separate method called is_anagram(word1, word2), that will compare 2 words and return True if they contain the same letters (but not in the same order), and False if not.

#     Note: None of the methods in the class should print anything.

# Step 1: Create the AnagramChecker Class

#     Create a class called AnagramChecker.
#     Implement the __init__ method:
#         Load the word list file into a variable (e.g., a set or list).
#         Store the words in lowercase for case-insensitive comparison.
class AnagramChecker:
    def __init__(self):
        with open('sowpods.txt', "r") as f:
            word_string = f.read().lower()
        self.word_set = set(word_string.split())

# Step 2: Implement is_valid_word Method

#     Create a method called is_valid_word(word).
#     Check if the given word exists in the loaded word list (case-insensitive).
#     Return True if valid, False otherwise.
    def is_valid_word(self, word):
        if word.lower() in self.word_set:
            return True
        return False
        
# Step 3: Implement is_anagram Method

#     Create a method called is_anagram(word1, word2).
#     Check if the sorted characters of word1 are equal to the sorted characters of word2.
#     Return True if anagrams, False otherwise.
    def is_anagram(self,word1,word2):
        if sorted(word1) == sorted(word2):
            return True
        return False
    

# Step 4: Implement get_anagrams Method

#     Create a method called get_anagrams(word).
#     Create an empty list to store anagrams.
#     Iterate through the word list.
#     For each word in the list, check if it’s an anagram of the given word using is_anagram.
#     If it’s an anagram and not the same word, add it to the anagrams list.
#     Return the list of anagrams.
    def get_anagrams(self,word):
        anagram_list = []
        for entry in self.word_set:
            if self.is_anagram(word,entry) and word != entry:
                anagram_list.append(entry)
        return anagram_list
    
# if __name__ == '__main__':
#     a1 = AnagramChecker()
#     test_value = a1.get_anagrams('dear')
#     print(test_value)
