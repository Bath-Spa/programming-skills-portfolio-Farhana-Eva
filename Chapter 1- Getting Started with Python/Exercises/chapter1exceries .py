## Exercise 1: Print Strings :ballot_box_with_check.
#Write a Python program to print the following string in a specific format.

#Twinkle, twinkle, little star,
	#How I wonder what you are! 
		#Up above the world so high,   		
		#Like a diamond in the sky. 
#Twinkle, twinkle, little star, 
	#How I wonder what you are!
#This is the solution of exercise

print("Twinkle,twinkle,little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle,twinkle,little star,\n\tHow I wonder what youare!")


## Exercise 2: Print the Version of Python :ballot_box_with_check:

 #Write a Python program to get the Python version you are using.
 #This is the solution of exercise

import sys
print("the python version you are using:")
print(sys.version)


## Exercise 3: Print date and Time :ballot_box_with_check:
#Write a Python program to display the current date and time.
#This is the solution of exercise
# importing date module

from datetime import date
today = date.today()

# dd/mm/yy
date1 = today.strftime('%d/%m/%Y')
print('date1 =', date1)

# Textual month, day and year
date2 = today.strftime('%B %d, %Y')
print('date2 =', date2)

# mm/dd/yy
date3 = today.strftime('%m/%d/%Y')
print('date3 =', date3)

# Month abbrevation , day and yeat
date4 = today.strftime('%b-%d-%Y')
print('date4 =', date4)


## Exercise 4: Strings Concatination :ballot_box_with_check:
#Write three strings in different variables and print the output as one string.

 #This is the solution of exercise
string1="I"
string2="LOVE"
string3="YOU"
print(string1," "+string2," "+string3)


## Exercise 5: Compute area of Circle :ballot_box_with_check:

#Write a Python program which accepts the radius of a circle from the user and compute the area.
#This is the solution of exercise
PI=3.14
Radius=float (input("enter the radius circle:"))
area_of_the_circle=PI*Radius*Radius
print("the area of the circle ", area_of_the_circle)
