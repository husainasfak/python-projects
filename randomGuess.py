import random

# User guessing
def guess(x):
     random_number = random.randint(1, x)
     guessedNumber = 0
     while guessedNumber != random_number:
          guessedNumber = int(input(f'Guess a number between 1 to {x}:'))
          if guessedNumber < random_number:
               print('Sorry guess again. Too low.')
          elif guessedNumber > random_number:
               print('Sorry, guess again. Too high')
     print(f"you guessed it right. the number was {random_number}")


# computer guessing
def computer_guess(x):
     low = 1
     high = x
     feedback = ''

     while feedback != 'c':
          guess  = random.randint(low, high)


guess(10)