import random
a = num = random.randint(1, 100)
print('''I have chosen a random number from 1 to 100.
You have 7 attempts to guess it.''')
for i in range(1,8):
    print(f'Chance {i}:')
    b = int(input('Guess the number: '))
    print(f'You guessed {b}.')
    if b == a:
        print('You guessed the number! Good job.')
        break
    elif b > a:
        print('Too high.')
    elif b < a:
        print('Too low.')

    if i ==7:
        print(f'Game Over! The number is {a}.')
