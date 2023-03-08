from QuestionMult import Question
"""LETS BUILD A MULTIPLE CHOICE QUESTION"""
#Lets thus create the first array of question prompts
question_prompts= [" What colour are aples ?:\n (a) Red/Green \n (b) Purple\n (c) Orange\n \n",
                   "What colour are bananas ? \n (a) Teal \n  (b) Magenta\n (c) Yellow \n \n"
                    "What colour are Strwaberries ? /n (a) Yellow\n (b) Red/n (c) Blue\n \n" ]
#Lets create another array of of question objects
questions= [
      Question(question_prompts[0] , "a"),#question_prompts[0] is the prompt, "a" is the answer, as from the class blue print in the constructor initiaalization
      Question(question_prompts[1] , "c"),
      Question(question_prompts[2] , "b") 
]#After this bracket, the next thing is to create a function that will run the test, as below-the below is functional approach, the above is OOPs oriented
def run_test(questions):#it will accept questions, and lets loop through each question.
     score= 0
     for question in questions:#ie, for each question object in the questions array, we want to do something
         answer= input(question_prompts) 
         if answer==question.answer:
              score+=1
         print("You got : " +str(score) + "/" + str(len(questions)) +"Correct ")
run_test(questions)