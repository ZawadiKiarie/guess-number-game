import random

def computer_guess(x):
  low = 1
  high = x
  feedback = ''
  guess_no = 0

  while feedback != 'c':
    if low != high:
      guess_no = random.randint(low, high) # ask kendi if she understood this logic
    else:
      guess_no = low # could also be high

    feedback = input(f"Is {guess_no} too high(H), too low(L) or correct(C): ").lower()

    if feedback == 'h':
      high = guess_no - 1
    elif feedback == 'l':
      low = guess_no + 1
  
  print(f"Yaay computer guessed your number, {guess_no} correctly!!")

computer_guess(1000)