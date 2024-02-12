#This is going to be my first python program. I will start with a simple hello world that takes the input of a user then output it back to the user.

name = input("Hello user, can you please give me your name?")
print('I have been told your name is ' + name + ". Can you confirm if this is true? ")

x = input("Please respond with 'yes' or 'no': ")

if x == 'Yes' or 'YES' or 'yes':
    print("You responded with '"+x+'! Thank you for confirming your name '+ name + ', I hope you have a good day!')
else:
    print("So your name is not " + name + '?')
