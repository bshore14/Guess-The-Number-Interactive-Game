import random
print("Hello, what is your name?")

name = input()
secretNum = random.randint(1,25)
print(f'{name}, I am thinking of a number between 1 and 25')

# Player will guess 5 times
for numguessed in range(1,8):
  print('Guess a number!')
  guess = int(input())
  if guess < secretNum:
    print("Your guess is too low!")
  elif guess > secretNum:
    print("Your guess is too high!")
  else:
    break
    
if guess == secretNum:
  print(f"Great job you guessed the secret number, {secretNum}")
else:
  print(f"Sorry, but the secret number was {secretNum}")