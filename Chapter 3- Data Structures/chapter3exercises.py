# Chapter 3: Exercises 

#Exercises with a tick mark :ballot_box_with_check: represent exercises that must be submitted as part of your Programming Skills Portfolio as a minimum expectation. Completing more exercises provides the opportunity to attain higher marks. For each exercise you should create a _**new project**_ with the name of the exercise and save it to this exercises folder in your local repository.

#Once you have completed your solution you should make sure you commit and push your solutions to your remote repository on GitHub. You can commit and push as many changes to your solutions as you wish, only those pushed before the chapter deadlines will be marked for the Programming Skills Portfolio.  


## Exercise 1: Names :ballot_box_with_check:

#Store the names of a few of your friends in a list called names. Print each person’s
# name by accessing each element in the list, one at atime.

#This is the solution of exercise

names = ["Asfa", "Iqra", "Eva"]

print(names[0])
print(names[1])
print(names[2])

## Exercise 2: Greetings :ballot_box_with_check:

#Start with the list you used in Exercise 1, but instead of just

#printing each person’s name, print a message to them.
#The text of each message should be the same, but each message should be 

#personalized with the person’s name.

#This is the solution of exercise

names = ["Asfa", "Iqra", "Eva"]

print("Hello, my good friend {}".format(names[0]))
print("Hello, my good friend {}".format(names[1]))
print("Hello, my good friend {}".format(names[2]))

## Exercise 3: Your Own List :ballot_box_with_check:

#Think of your favorite mode of transportation, such as a motorcycle or a car,
# and make a list that stores several examples. Use your list
#to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

#This is the solution of exercise
favorite_transportation = ['car', "airplane"]

print("I go to work using {}".format(favorite_transportation[0]))
print("I travel overseas using {}".format(favorite_transportation[1]))


## Exercise 4: Guest List :ballot_box_with_check:

#If you could invite anyone, living or deceased, to dinner, 
#who would you invite? Make a list that includes at least three people you’d

#like to invite to dinner. Then use your list to print a message to each person, invitingthem to dinner.

#This is the solution of exercise
guests = ['Asfa', 'Iqra', 'Nipa']

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

## Exercise 5: Change Guest List :ballot_box_with_check:

#You just heard that one of your guests can’t make the
#dinner, so you need to send out a new set of invitations. You’ll have to think of
#someone else to invite.

#•Start with your program from Exercise 3-4. 
#Add a print() call at the end of your program stating the name of the guest who can’t make it.

#•Modify your list, replacing the name of the guest who can’t make it with the name of 
#the new person you are inviting.

#•Print a second set of invitation messages, one for each person who is still in your list.

#This is the solution of exercise
#Invite some people to dinner.
guests = ['Asfa', 'Nipa', 'Iqra']

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print("\nSorry, " + name + " can't make it to dinner.")

# Nipa can't make it! Let's invite Aisha instead.
del(guests[1])
guests.insert(1, 'Aisha')

# Print the invitations again.
name = guests[0].title()
print("\n" + name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")


## Exercise 6: Shrinking Guest List :ballot_box_with_check:

#You just found out that your new dinner table won’t arrive in time for the dinner, 
#and you have space for only two guests.

#•Start with your program from Exercise 3-5. 
#Add a new line that prints a message saying that you can invite only two people for dinner.

#•Use pop() to remove guests from your list one at a time until only two names remain in your list.
# Each time you pop a name from your list, print a message to that person letting 
#them know you’re sorry you can’t invite them to dinner.

#•Print a message to each of the two people still on your list, letting them know they’re still invited.

#•Use del to remove the last two names from your list, so you have an empty list.
# Print your list to make sure you actually have an empty list at the end of your program.

#This is the solution of exercise
#Invite some people to dinner.
guests = ['Asfa', 'nipa', 'Iqra']

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print("\nSorry, " + name + " can't make it to dinner.")

# Nipa can't make it! Let's invite Aisha instead.
del(guests[1])
guests.insert(1, 'Aisha')

# Print the invitations again.
name = guests[0].title()
print("\n" + name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

# We got a bigger table, so let's add some more people to the list.
print("\nWe got a bigger table!")
guests.insert(0, 'Nayma')
guests.insert(2, 'jery')
guests.append('mitu')

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[3].title()
print(name + ", please come to dinner.")

name = guests[4].title()
print(name + ", please come to dinner.")

name = guests[5].title()
print(name + ", please come to dinner.")

# Oh no, the table won't arrive on time!
print("\nSorry, we can only invite two people to dinner.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

# There should be two people left. Let's invite them.
name = guests[0].title()
print(name + ", please come to dinner.")
name = guests[1].title()
print(name + ", please come to dinner.")

# Empty out the list.
del(guests[0])
del(guests[0])

# Prove the list is empty.
print(guests)


## Exercise 7: Seeing the World :ballot_box_with_check:
#Think of at least five places in the world you’d like to visit.
#•	 Store the locations in a list. Make sure the list is not in alphabetical order.

#•	 Print your list in its original order.
# Don’t worry about printing the list neatly,just print it as a raw Python list.

#•	 Use sorted() to print your list in alphabetical order without modifying the actual list.

#•	 Show that your list is still in its original order by printing it.

#•	 Use sorted() to print your list in reverse alphabetical order
# without changing the order of the original list.

#•	 Show that your list is still in its original order by printing it again.

#•	 Use reverse() to change the order of your list. Print the list to show that its order has changed.

#•	 Use reverse() to change the order of your list again.
# Print the list to show it’s back to its original order.

#•	 Use sort() to change your list so it’s stored in alphabetical order. 
#Print the list to show that its order has been changed.

#•	 Use sort() to change your list so it’s stored in reverse alphabetical order.
# Print the list to show that its order has changed.

#This is the solution of exercise
locations = ['Uyuni salt flat', 'Cape town', 'Sentorini', 'Paris', 'Venice']

print("Original order:")
print(locations)

print("\nAlphabetical:")
print(sorted(locations))

print("\nOriginal order:")
print(locations)

print("\nReverse alphabetical:")
print(sorted(locations, reverse=True))

print("\nOriginal order:")
print(locations)

print("\nReversed:")
locations.reverse()
print(locations)

print("\nOriginal order:")
locations.reverse()
print(locations)

print("\nAlphabetical")
locations.sort()
print(locations)

print("\nReverse alphabetical")
locations.sort(reverse=True)
print(locations)

