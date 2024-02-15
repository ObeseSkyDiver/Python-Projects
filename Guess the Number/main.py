import random

#Introduction for the user
print("Welcome to the guessing game! You will have to guess what number the system has generated.")

#We will ask the user to choice what range they want the number to be from.
print("Please input the range you want your random number to be between. Please make the first number lower than the second number if possible. :)")
x = int(input("Please input the first number: "))
y = int(input("Please input your second number: "))

#Taking the varibles inputted from the user and using them as the range for our guessing game.
result = random.randrange(x,y)

#Ask the user to start guessing what the number is.
print("Welcome to the start of the guessing game. You will have to guess the random number that the system made up. Good luck!")

#initialize the variable to be used in our loop. Also initialize a varible to track attemps
U_input = 0
attempts = 0

#While loop that will ask the user to guess a number and then inform them if they are low or high.
while U_input != result:

    U_input = int(input("Please guess what the number is:"))
    attempts += 1

    if U_input < result:
        print("The number is too low.")

    elif U_input > result:
        print("The number is too high.")

    else:
        print(f"Good job! That was some luck! You finished it in {attempts} attempts!")