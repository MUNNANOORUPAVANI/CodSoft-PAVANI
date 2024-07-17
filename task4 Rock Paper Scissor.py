# GAME:ROCK PAPER SCISSOR
def check_guess(guess,answer):
 global scoresc
 still_guessing = True
 attempt = 0
 while still_guessing and attempt < 3:
  if guess.lower() == answer.lower():
    print("correct answer")
    score = score+1
    still_guessing =False
  else:
     if attempt<2:
       guess = input("sorry wrong answer, try again")
     attempt = attempt+1
     if attempt == 3:
       print("the correct answer is", answer)
 score = 0
print("guess the CORRECT ANSWER?")
guess1 = input("rock smashes the paper")
check_guess(guess1,"rock")
guess2 = input("paper cover the rock")
check_guess(guess2,"paper")
guess3 = input("scissor cuts the paper")
check_guess(guess3,"scissor")