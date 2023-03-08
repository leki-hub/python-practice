""" The expanation is in freecode camp youtube 4 hrs,26 min tutorial, at 2hrs 20 min"""
secret_word= "Possible"
guess= " " 
guess_limit= 3
Trials= 0
Outof_Trials= False
while guess !=secret_word and not (Outof_Trials) :
   if Trials< guess_limit:
    guess=  input("Enter the gause value : ")
    Trials +=1
   else:
      Outof_Trials = True
if Outof_Trials:
   print("Out of Trials limit, You lose ! ")
else:
   print("You've won !")
  #Example 2.
  
secret_word = input("Enter the secret word: ")

print("\nThe secret word has been set. You have 10 tries to guess the word.")

for i in range(10):
    guess = input("Enter your guess: ")
    if guess == secret_word:
        print("\nCongratulations! You've guessed the secret word in", i+1, "tries.")
        break
    else:
        print("\nIncorrect. Try again.")

if guess != secret_word:
    print("\nSorry, you've run out of tries. The secret word was", secret_word + ".")
# Example 3
import random

def guess_number():
    secret_number = random.randint(1, 100)
    tries = 0

    print("\nI'm thinking of a number between 1 and 100. Can you guess it?")

    while tries < 7:
        guess = int(input("Enter your guess: "))
        tries += 1

        if guess < secret_number:
            print("Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print("\nCongratulations! You've guessed the secret number in", tries, "tries.")
            break

    if tries == 7:
        print("\nSorry, you've run out of tries. The secret number was", secret_number + ".")

guess_number()
 #Example 
import random
randomNum = random.randint(1, 5)
score = 6 #Initialization
while score > 0:
    Guess = int(input("Enter your guess value: "))
    score -= 1
    if Guess == randomNum:
        print("Congratulations, you've won and score is ", str(score))
        break
    else:
        print("Try next time")
if score <= 0:
    print("You have run out of tries.")
 #or 
import random
randomNum= random.randint(1,5)
score =0 #Initialization
while score<=6:
  Guess= int(input("Enter you guess value : "))
  score+=1
  if Guess== randomNum:
    print("Congratulations , yo've won  and score is  ",str(score) )
    break
  else:
    print(" Try next time ")
if score >6:
    print( " You ARE out of trials") 
#this  below can also work, but its incomlete, ie does not dsplay if False is encountered.
import random
randomNum= random.randint(1,5)
score =6 #Initialization
while True:
  Guess= int(input("Enter you guess value : "))
  score-=1
  if Guess== randomNum:
    print("Congratulations , yo've won  and score is  ",str(score) )
    break#Nb we break whenever the no more itetaion is needed,else continue will work by default
  else:
    print(" Try next time ")