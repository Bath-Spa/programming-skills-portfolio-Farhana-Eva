# Chapter 7 Exercises

#Exercises with a tick mark :ballot_box_with_check: represent exercises that must be submitted as part of your Programming Skills Portfolio as a minimum expectation. Completing more exercises provides the opportunity to attain higher marks. For each exercise you should create a _**new project**_ with the name of the exercise and save it to this exercises folder in your local repository.

#Once you have completed your solution you should make sure you commit and push your solutions to your remote repository on GitHub. You can commit and push as many changes to your solutions as you wish, only those pushed before the chapter deadlines will be marked for the Programming Skills Portfolio.  

## Exercise 1:   Message  :ballot_box_with_check:

#Write a function called display_message() that prints one sentence telling everyone
# what you are learning about in this chapter. Call thefunction,
# and make sure the message displays correctly.
#This is the solution of exercise
def display_message():
    """Display a message about what I'm learning."""
    msg = "I'm learning to store code in functions."
    print(msg)

display_message()

## Exercise 2: Favorite Book :ballot_box_with_check:
#Write a function called favorite_book() that accepts one parameter, title. 
#The function should print a message, such as One of myfavorite books is Alice in Wonderland.
# Call the function, making sure to include a book title as an argument in the function call.
#This is the solution of exercise
def favorite_book(title):
    """Display a message about someone's favorite book."""
    print(title + " is one of my favorite books.")

favorite_book('The Abstract Wild')

## Exercise 3: T-Shirt  :ballot_box_with_check:

#Write a function called make_shirt() that accepts a size and the text of a message 
#that should be printed on the shirt. The function should print a sentence summarizing 
#the size of the shirt and the message printed on it. Call the function once using positional 
#arguments to make a shirt. Call the function a second time using keyword arguments.
#This is the solution of exercise
def make_shirt(size, message):
    """Summarize the shirt that's going to be made."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt('large', 'I love Python!')
make_shirt(message="Readability counts.", size='medium')

## Exercise 4:  Large Shirts :ballot_box_with_check:

#Modify the make_shirt() function so that shirts are large by default
# with a message that reads I love Python. Make a large shirt and a
#medium shirt with the default message, and a shirt of any size with a different message.
#This is the solution of exercise
def make_shirt(size='large', message='I love Python!'):
    """Summarize the shirt that's going to be made."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Programmers are loopy.')

## Exercise 5: Cities

#Write a function called describe_city() that accepts the name of a city and its country.
 #The function should print a simple sentence, such as Reykjavik is in Iceland.
# Give the parameter for the country a default value.
#Call your function for three different cities, at least one of which is not in the default country.
#This is the solution of exercise
def describe_city(city, country='chile'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('santiago')
describe_city('reykjavik', 'iceland')
describe_city('punta arenas')





