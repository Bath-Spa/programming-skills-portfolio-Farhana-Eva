# Chapter 6 Exercises
#Exercises with a tick mark :ballot_box_with_check: represent exercises that must be submitted as part of your Programming Skills Portfolio as a minimum expectation. Completing more exercises provides the opportunity to attain higher marks. For each exercise you should create a _**new project**_ with the name of the exercise and save it to this exercises folder in your local repository.

#Once you have completed your solution you should make sure you commit and push your solutions to your remote repository on GitHub. You can commit and push as many changes to your solutions as you wish, only those pushed before the chapter deadlines will be marked for the Programming Skills Portfolio.  


## Exercise 1: Pizza Toppings :ballot_box_with_check:

#Write a loop that prompts the user to enter a series of pizza toppings until they 
#enter a 'quit' value. As they enter each topping,

#print a message saying you’ll add that topping to their pizza.

#This is the solution of exercise
prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break



## Exercise 2: Movie Tickets: :ballot_box_with_check:

#A movie theater charges different ticket prices depending on a person’s age. If a person
# is under the age of 3, the ticket is free; if

#they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15.
# Write a loop in which you ask users their 

#age, and then tell them the cost of their movie ticket

#This is the solution of exercise
prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")



## Exercise 3: Infinity :ballot_box_with_check:

#Write a loop that never ends, and run it. (To end the loop, press ctrl-C or close 
#the window displaying the output.)

#This is the solution of exercise







## Exercise 4: Deli :ballot_box_with_check:

#Make a list called sandwich_orders and fill it with the names of various sandwiches. 
# Then make an empty list called finished_sandwiches.

#Loop through the list of sandwich orders and print a message for each order,
# such as I made your tuna sandwich. As each sandwich is made, 

#move it to the list of finished sandwiches. After all the sandwiches have been made,
# print a message listing each sandwich that was made.

#This is the solution of exercise

sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")


## Exercise 5: No Pastrami :ballot_box_with_check:

#Using the list sandwich_orders from Exercise 7-8, make sure 
#the sandwich 'pastrami' appears in the list at least three times. Add code

#near the beginning of your program to print a message saying
# the deli has run out of pastrami, and then use a while loop to remove all 

#occurrences of 'pastrami' from sandwich_orders. 
#Make sure no pastrami sandwiches end up in finished_sandwiches.

#This is the solution of exercise
sandwich_orders = [
    'pastrami', 'veggie', 'grilled cheese', 'pastrami',
    'turkey', 'roast beef', 'pastrami']
finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")

