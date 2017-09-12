import random
from sys import exit
# get random number
number = random.randint(0, 20)

i = 0
while i < 10:
    print("please input a guess number")
    try:
        guess_num = int(input('>'))


        if guess_num < number:
            print(f"your guess number {guess_num} is too small")


        elif guess_num > number:
            print(f"your guess number {guess_num} is too big")

        else:
            print("you guess right")
            exit(0)
    except ValueError:
        print("请输入数字")

    lef_times = 9 - i
    if(lef_times == 0):
        print("no chance left")
    else:
        print(f"you still have {lef_times} chance")

    i += 1

