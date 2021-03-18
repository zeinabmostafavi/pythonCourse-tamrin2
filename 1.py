import random

computer_number = random.randint(0, 20)
counter = 0

while True:
    user_numner = int(input())
    counter += 1

    if user_numner == computer_number:
        print('you win!', 'number of your tries:', counter)
        break
    elif user_numner > computer_number:
        print('boro paeen')
    elif user_numner < computer_number:
        print('boro bala')
