import random
randomNum= random.randint(1,70)
score =0
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
  #Or 
import random
randomNum = random.randint(1, 5)
score = 6
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
"""or """ #If we wish to use a function
import random
randomNum= random.randint(1,10)
def randomnum():  
 score=0
 while score<=7:
  Guess= int(input("Enter you guess value : "))
  score+=1
  if Guess== randomNum:
    print("Congratulations , yo've won  and score is  ",str(score) )
    break
  else:
    print(" Try next time ")
 if score >6:
    print( " You ARE out of trials") 

print(randomnum())
