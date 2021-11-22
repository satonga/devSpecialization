# A number-guessing game
from random import randint

# intro block
print("Hello player, what`s your name?")
name = input("Enter name: ")
print(
    "Hi " + name + " I'm thinking of a number between 1 and 100.\nTry to guess my number."
    )

num = randint(1 , 100)
count = 0

while True:
    try:
        count += 1
        guess = int(input('Your guess? '))
        if (guess > num):
            print('Your guess is too high, try again')
        elif (guess < num):
            print('Your guess is too low, try again.')
        else:
            print('Good job ' + name + '! You guessed my number in ' + str(count) + ' tries!')
            break
    except ValueError:
        print('Please input a number for your guess.')
    except:
        print('Something went wrong...Try again.')
