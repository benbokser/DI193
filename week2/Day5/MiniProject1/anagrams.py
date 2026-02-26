# Now create another Python file, called anagrams.py. This will contain all the UI (user interface) functionality of your program, and will rely on AnagramChecker for the anagram-related logic.

# It should do the following:
# Step 1: Import AnagramChecker
from anagram_checker import AnagramChecker

# Step 2: Create a Menu Loop
#     Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.
while True:
    print('This program finds anagrams based on the word you input.')
    selection = input('Input a word or type E to exit.').strip()

# Step 3: Get User Input and Validate
#     If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then be validated:
#         Only a single word is allowed. If the user typed more than one word, show an error message. (Hint: how do we know how many words were typed?)
#         Only alphabetic characters are allowed. No numbers or special characters.
#         Whitespace should be removed from the start and end of the user’s input.
    if selection == 'E':
        break
    if selection.isalpha() == False:
        print('Only letters allowed in the word. No spaces, numbers, or other characters.')
        continue




    


# Step 4: Find and Display Anagrams

#     Create an instance of AnagramChecker.
#     Use is_valid_word to check if the word is valid.

#     Use get_anagrams to find anagrams.
#     Display the word, its validity, and the anagrams in a formatted message.

#     Once your code has decided that the user’s input is valid, it should find out the following:
#         All possible anagrams to the user’s word.
#         Create an AnagramChecker instance and apply it to the steps created above.
#         Display the information about the word in a user-friendly, nicely-formatted message such as:


#         YOUR WORD :”MEAT”
#         this is a valid English word.
#         Anagrams for your word: mate, tame, team.

    a1 = AnagramChecker()
    validity_check = a1.is_valid_word(selection)
    if validity_check == False:
        print('Not a valid word.')
        continue
    anagrams = a1.get_anagrams(selection)
    print(f'''Your word: {selection}
This is a valid English word.
Anagrams for your word: {', '.join(anagrams)}
''')

