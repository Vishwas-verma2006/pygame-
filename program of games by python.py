program of game (snake , water , gun) with loop
'''
here -1 is water 
1 is snake
0 is gun
'''
def play():
    
    import random 
    #computer = -1
    computer = random.choice([-1,1,0])
    # this below is dictionaries and variables 

    youstr = input("Enter your choice: ")
    youdict = {"s" : 1 , "w" : -1 , "g" : 0}
    you = youdict[youstr]
    reverserdict = {1 : "Snake" , -1 : "Water" , 0 : "Gun"}

    print(f"You Entered: {reverserdict[you]}")
    print(f"Computer Entered: {reverserdict[computer]}\n")

    # Apply codnditions 

    if (computer == you):
        print("Its draw 🙌 !")
    
    else :
        if (computer == 1 and you == -1):
            print("You loose 😫 ")
        
        if (computer == -1 and you ==0 ):
            print("You loose 😫 ")
        
        if (computer == 0 and you == 1):
            print("You loose 😫 ")
        
        if (computer == 1 and you == 0):
            print("You Win 👍 ")
        
        if (computer == -1  and you == 1):
            print("You Win 👍 ")
        
        if (computer == 0 and you == -1):
            print("You Win 👍 ")
        
    
while True:
    print("1. PLAY ~")
    print("2. EXIT !")
    choice = input("Enter you choice: ")
    if choice == "1":
        play()
    else :
        print("Exiting from game !")
        break



program of game (snake, water , gun) WITHOUT LOOP 

import random 
#computer = -1
computer = random.choice([-1,1,0])
# this below is dictionaries and variables 

youstr = input("Enter your choice: ")
youdict = {"s" : 1 , "w" : -1 , "g" : 0}
you = youdict[youstr]
reverserdict = {1 : "Snake" , -1 : "Water" , 0 : "Gun"}

print(f"You Entered: {reverserdict[you]}")
print(f"Computer Entered: {reverserdict[computer]}\n")

# Apply codnditions 

if (computer == you):
    print("Its draw 🙌 !")
    
else :
    if (computer == 1 and you == -1):
        print("You loose 😫 ")
        
    if (computer == -1 and you ==0 ):
        print("You loose 😫 ")
        
    if (computer == 0 and you == 1):
        print("You loose 😫 ")
        
    if (computer == 1 and you == 0):
        print("You Win 👍 ")
        
    if (computer == -1  and you == 1):
        print("You Win 👍 ")
        
    if (computer == 0 and you == -1):
        print("You Win 👍 ")


#program of snake,water,gun game by short method using pattern form 

import random 

computer = random.choice([-1,0,1])
youstr = input("Enter your choice:- ")
youdict= {"s":1, "w":-1, "g":0}
reversedict = { 1:"Snake", -1:"Water", 0:"Gun"}
you = youdict[youstr]

print(f"Computer Choosed: {reversedict[computer]}\nYou Choosed {reversedict[you]}")


if (computer == -1 or computer == 2):
    print("You Loose !")
elif (computer == you):
    print("Its Draw ---")
else:
    print("You Win ~")
    
    
'''if (computer == you):
    print("Its tie")
    
else :
    if (computer == -1 and you == 0): # -1-0=-1 here we just substtract the value of integer form 
        print("Computer win")  # then we make a patter that in which interger you win or loose 
        
    if (computer == 1 and you == -1): #1--1=2
        print("Computer win")
        
    if (computer == 0 and you == 1): #0-1=-1
        print("Computer win")
        
    if (computer == 1 and you == 0): #1-0=1
        print("You win")
        
    if (computer == -1 and you == 1): #-1-1=-2
        print("You win") 
        
    if (computer == 0 and you == -1): # 0--1=1
        print("You win")'''
        