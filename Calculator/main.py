#Defining the functions we will use for this calculator program.
def add(x,y):
    print(x, '+', y)
    z = x + y
    return print("The sum is ", z)

def subtract(x,y):
    print(x, '-', y)
    z = x - y
    return print("The difference is ", z)

def multiply(x,y):
    print(x, '*', y)
    z = x * y
    return print("The product is ", z)

def divide(x,y):
    print(x, '/' ,y)
    z = x / y
    return print("The answer is ",z)

def power(x,y):
    print(x, '^' ,y)
    z = x ** y
    return print(z)


#We will identify the user so we can know who we are dealing with.
name = input("Hello, can I please get your name before we start?")

#This will output the users name and inform them of what to expect. 
print("Okay,",name,"this is your personal calculator program. I will help you with basic mathematics(such as addition, subtraction, multiplication, division, and powers).")

#Allow user to pick what kind of mathematics they want to do.
print("""Please choose what type of mathematics we will do. Please type down the number choice to make it simplier
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Power""")
choice = input("Input your choice: ")

#The user will make a choice of what math they want to do.
if choice == '1':
    print("We are doing addition!")
    x = float(input("Please input your first number: "))
    y = float(input("Please input your second number: "))
    add(x,y)
elif choice == '2':
    print("We are subtracting!")
    x = float(input("Please input your first number: "))
    y = float(input("Please input your second number: "))
    subtract(x,y)
elif choice == '3':
    print("We are going to multiply!")
    x = float(input("Please input your first number: "))
    y = float(input("Please input your second number: "))
    multiply(x,y)
elif choice == '4':
    print("We are going to divide some numbers!")
    x = float(input("Please input your first number: "))
    y = float(input("Please input your second number: "))
    divide(x,y)
elif choice == '5':
    print("It's time for powers!")
    x = float(input("Please input your first number: "))
    y = float(input("Please input what power you want: "))
    power(x,y)
else: ValueError
print(choice," is not a valid option. Please try again!")

