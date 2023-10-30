## Exercise 1: Variables:ballot_box_with_check:


#Assign a message to a variable, and print that message.
#Then change the value of the variable to a new message, and print the new
#message.

#This is the solution of exercise
massage="this is the value of the variable to a new massage "
print(massage)
massage="a new massage"
print(massage)


## Exercise 2: Variables :ballot_box_with_check:

#Find a quote from a famous person you admire. Print the quote and the name of its author. 

#Your output should look something like the following, including the quotation marks:

#Albert Einstein once said, “A person who never made a mistake never tried anything new.

#This is the solution of exercise
print('Humayun Ahmed once said,"success is not permanent,failure is not fatal-it is the courage to continue that counts.')


## Exexcise 3: ripping Names :ballot_box_with_check:

#Tidy up the code to make it easier to understand

#Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, “\t” and “\n”, at least once.

#Print the name once, so the whitespace around the name is displayed. 

#Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

#This is the solution of exercise
#python code using stripping
#string
a="\FARHANA EVA\n"
print(a)
print(a.lstrip())
print(a.rstrip())
print(a.strip())


## Exercise 4: Favorite Number :ballot_box_with_check:
#Use a variable to represent your favorite number. Then,using that variable, create a message that reveals your favorite number. Print
#that message.
#This is the solution of exercise
favorite_number=25
print("my favorite_number is",favorite_number)



## Exercise 5: USB Shopper :ballot_box_with_check:

#A girl heads to a computer shop to buy some USB sticks. 
#She loves USB sticks and wants as many as she can get for £50. They are £6 each.

#Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.

#You will to use the arithmetic operators to complete this exercise.
#This is the solution of exercise
USB_Bought=("Total USB bought are=")
money_left="Total money that is left="
print(USB_Bought+str(int(50/6)))
print(money_left+str(50%6))







