import random

def guess(x):
  random_no = random.randint(1, x)
  guess_no = 0 #question to ask kendi, why we need to predefine it with 0

  while guess_no != random_no:
    guess_no = int(input(f"Guess a number between 1 and {x}: "))
    
    if guess_no < random_no:
      print("Sorry, try again. Too Low")
    elif guess_no > random_no:
      print("Sorry, try again. Too high")

  print(f"Yaay!! You guessed the number {random_no} correctly")

guess(10)