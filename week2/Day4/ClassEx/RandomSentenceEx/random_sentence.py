# 🌟 Exercise 1 — Random Sentence Generator
import random

def get_words_from_file(file_path):
    with open(file_path, "r") as f:
        content = f.read()
# content is ONE big string - split it into words
    return content.split()


def get_random_sentence(length):
# pick random words, join, return lowercase
    word_list = get_words_from_file('words.txt')
    random_list = [random.choice(word_list) for _ in range(length)]
    random_string = ' '.join(random_list)
    return random_string.lower()


def main():
      # get input, validate, generate sentence
    try:
        number = int(input('Enter sentence length(2-20):'))
        print(f"You entered: {number}")
    except ValueError:
        print(f"'Invalid input. Please enter a number.")
        return
    if not 2 <= number <= 20:
        print(f'Please enter a number between 2 and 20')
        return
    
    sentence = get_random_sentence(number)
    print(f'Generated sentence: {sentence}')

main()



# def get_number():
#     user_input = "hello"  # simulate bad input
#     try:
#         number = int(user_input)
#         print(f"You entered: {number}")
#     except ValueError:
#         print(f"'{user_input}' is not a valid number!")


# get_number()


# def get_number_good():
#     user_input = "42"  # simulate good input
#     try:
#         number = int(user_input)
#         print(f"You entered: {number}")
#     except ValueError:
#         print(f"'{user_input}' is not a valid number!")


# get_number_good()