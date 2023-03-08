#This is a simple while loop that will continue to prompt the user for input until they enter the word "exit"  If the input is not a number, it will prompt them to enter a number again. 
# ...If the input is not between 1 and 10, it will prompt them to enter a number between 1 and 10 again.When the user enters a valid number between 1 and 10 or "exit" the loop will exit.
#This is thus an infinite loop.
while True:
    user_input = input("Enter a number between 1 and 10:")
    if user_input == "exit":
        print("Exiting the loop.")
        break
    elif not user_input.isdigit():
        print("Invalid input. Please enter a number.")
        continue
    elif int(user_input) < 1 or int(user_input) > 10:
        print("Invalid number. Please enter a number between 1 and 10.")
        continue
    else:
        print("Thank you for entering the number:", user_input)
"""EXAMPLE 2"""
# Years= [2005, 2006, 2007, 2008, 2009, 2010]
# index= 0
# Year= Years[0]
# while True:
#     if Year== 2008:
#         break
#     print(Year)
#     index +=1
#     Year= Years[index]
# print("We have checked  only " ,index ,"counts")#Its out of the loop, ie optional
# print(f"The output obtained is to index {index}") # ,optional .Just learning how string format special method is uses
#  #Or
# years = [2005, 2006, 2007, 2008, 2009, 2010]
# index = 0
# year = years[0]
# while year !=2008:
#  print(year)
#  index+=1
#  year = years[index]
# print('It gives us only', index, 'repetititons to get out of loop')
#    #Example 3- in while loop, not all situations we use break or continue 
# """print the movie ratings gretater than 6."""
# movie_rating = [8.0, 7.5, 5.4, 9.1, 6.3, 6.5, 2.1, 4.8, 3.3]
# index = 0
# rating = movie_rating[0]
# while rating>=6:
#  print(rating)
#  index += 1
#  rating = movie_rating[index]
# print(' nb; There is only', index, 'movie rating, because the loop stops when it meets with the number lower than 6.')

# # Print the movie ratings gretater than 6.
# movie_rating = [8.0, 7.5, 5.4, 9.1, 6.3, 6.5, 2.1, 4.8, 3.3]
# index = 0
# for i in range(len(movie_rating)):
#  if movie_rating[i] >= 6:
#   index += 1
#  print(index, movie_rating[i])
# print('There is only', index, 'films gretater than movie rating 6 ,nb #This for loop will print any number greater than 6 , unlike the while loop')
#   #Example 
# # Adding the element in a list to a new list 
# fruits = ['banana', 'apple', 'banana', 'orange', 'kiwi', 'banana', 'Cherry', 'Grapes']
# new_fruits = []
# index = 0
# while fruits[index]  =="banana":
#  new_fruits.append(fruits[index])
#  index += 1
# print(new_fruits) #Output is ["banana"]