import random
import sys
import string

def Game():

    user_choice = int(input("Scissor(0), Rock(1), Paper(2):\n"))

    if user_choice == 0:
        x = "Scissor"
    elif user_choice == 1:
        x = "Rock"
    else:
        x = "Paper"

    cpu_choice = random.randint(0, 2)

    if cpu_choice == 0:
        y = "Scissor"
    elif cpu_choice == 1:
        y = "Rock"
    else:
        y = "Paper"

    if (user_choice == 0 and cpu_choice == 2) or (user_choice == 1 and cpu_choice == 0) \
    or (user_choice == 2 and cpu_choice == 1):
        print(f"User chose: {x}\nCPU chose: {y}\nUser Wins!")
    elif (user_choice == 0 and cpu_choice == 1) or (user_choice == 1 and cpu_choice == 2) \
    or (user_choice == 2 and cpu_choice == 0):
        print(f"User chose: {x}\nCPU chose: {y}\nCPU Wins!")
    else:
        print(f"User chose: {x}\nCPU chose: {y}\nTie Game!")

    w = input("Would you wish to play again? Y/N\n")

    if w == 'y' or w == 'Y':
        Game()
    elif w == 'n' or w == 'N':
        print("Please leave a review.\nThank you")
        sys.exit()

#Game()

def Comparer():

    y = ['A', 'B', 'C', 'D',
         'E', 'F', 'G', 'H',
         'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P',
         'Q', 'R', 'S', 'T',
         'U', 'V', 'W', 'X', 'Y', 'Z']
    
    char = input("Please enter your character: ")
    
    x = random.choice(y)
    
    print(f"The Random number is: {x}")
    
    if char == x:
        print("Equal")
    else:
        print("Not Equal")

#Comparer()

def oddNbr():
    
    while True:
        k = int(input("Please enter your number, press -1 to exit:\n"))
        if k != -1:
            for i in range(k+1):
                if i % 2 != 0:
                    print(i, end = ' ')
        else:
            break

#oddNbr()

def zeroExitor():

    while True:
        x  = int(input())
        if x == 0:
            print("Out of loop")
            break
        else:
            print(f"You entered {x}")
            
#zeroExitor()

def PasswordGenerator():
    nbrs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    x = int(input("Password Length: "))
    output = ''
    
    for i in range(x):
        output += random.choice(string.ascii_letters)
        output += random.choice(nbrs)
        
    for f in range(x):
        output = output.replace(random.choice(output[random.randrange(x+1)]), '')
    
    print(output)
    
#PasswordGenerator()
