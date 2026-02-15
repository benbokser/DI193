# Exercise 5: Longest word without a specific character
# Instructions

#     Keep asking the user to input the longest sentence they can without the character “A”.
#     Each time a user successfully sets a new longest sentence, print a congratulations message.
record = 0
for i in range(1,11):
    print(f'Input {i} out of 10.')
    sentence = input('Input the longest sentence you can without the character "a".')
    if 'A' in sentence or 'a' in sentence:
        print('That sentence contains "a"!')
    else:
        if len(sentence) > record:
            print('Congratulations! That sentence sets a new record for longest sentence without "a".')
            record = len(sentence)
        else:
            print('That sentence is not longer than your previous record.')