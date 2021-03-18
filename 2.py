import random

message = input("start(press any key)")
number = random.randint(1, 6)
print(number)

if number == 6:
    print("______   ______")
    print("***** 6 ******")
    print("______   ______")
    while(True):
        message = input("repeat(press any key)")
        number = random.randint(1, 6)
        print(number)
        if number != 6:
            print('End game')
            break
        else:
            print("***** 6 ******")

else:
    print('End game')
