# 🌟 Exercise 1 — Random Sentence Generator


# Step 1: Create the get_words_from_file function

#     Create a function named get_words_from_file that takes the file path as an argument.
#     Open the file in read mode ("r").
#     Read the file content.
#     Split the content into a list of words.
#     Return the list of words.


import random

def get_words_from_file(file_path):
    with open(file_path, "r") as f:
        content = f.read()
# content is ONE big string - split it into words
    return content.split()

# Step 2: Create the get_random_sentence function

#     Create a function named get_random_sentence that takes the sentence length as an argument.
#     Call get_words_from_file to get the list of words.
#     Select a random word from the list length times.
#     Create a sentence with the selected words.
#     Convert the sentence to lowercase.
#     Return the sentence.


def get_random_sentence(length):
# pick random words, join, return lowercase
    word_list = get_words_from_file('words.txt')
    random_list = [random.choice(word_list) for _ in range(length)]
    random_string = ' '.join(random_list).lower()
    return random_string

# Step 3: Create the main function

#     Create a function named main.
#     Print a message explaining the program’s purpose.
#     Ask the user for the desired sentence length.
#     Validate the user input:
#         Check if it is an integer.
#         Check if it is between 2 and 20 (inclusive).
#     If the input is invalid, print an error message and exit.
#     If the input is valid, call get_random_sentence with the length and print the generated sentence.

def main():
    print('This program generates a sentence of random words of user-selected length.')
      # get input, validate, generate sentence
    try:
        number = int(input('Enter sentence length(2-20):'))
        print(f"You entered: {number}")
    except ValueError:
        print(f"'Invalid input. Please enter a number.")
        return
    if not 2 <= number <= 20:
        print(f'Please enter a number between 2 and 20.')
        return
    
    sentence = get_random_sentence(number)
    print(f'Generated sentence: {sentence}')


# 🌟 Exercise 2: Working with JSON

# Instructions:

# Using the follow code:



# Step 1: Load the JSON string

#     Import the json module.
#     Use json.loads() to parse the JSON string into a Python dictionary.
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
data = json.loads(sampleJson)

# Step 2: Access the nested “salary” key
#     Access the “salary” key using nested dictionary access (e.g., data["company"]["employee"]["payable"]["salary"]).
#     Print the value of the “salary” key.
salary = data['company']['employee']['payable']['salary']
print(salary)


# Step 3: Add the “birth_date” key
#     Add a new key-value pair to the “employee” dictionary: "birth_date": "YYYY-MM-DD".
#     Replace "YYYY-MM-DD" with an actual date.
data['company']['employee']['birth_date'] = '1990-05-15'

# Step 4: Save the JSON to a file

#     Open a file in write mode ("w").
#     Use json.dump() to write the modified dictionary to the file in JSON format.
#     Use the indent parameter to make the JSON file more readable.
with open("employee.json", "w") as f:
    json.dump(data, f, indent=2)

if __name__ == '__main__':
    with open("employee.json", "r") as f:
        loaded = json.load(f)

    print(loaded)

