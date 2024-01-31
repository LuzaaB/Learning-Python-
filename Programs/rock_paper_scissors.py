import random

print("Winning rules of the game Rock Paper Scissors are :\n"
      +"Rock vs Paper -> Paper wins \n"
      +"Rock vs Scissors -> Rock wins \n"
      +"Paper vs Scissors -> Scissors wins \n")

while True :
    
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    # Taking input from the user
    choice = int(input("Enter your choice :"))
    
    # Looping until the user enters a valid input
    while choice > 3 or choice < 1 :
        choice = int(input('Enter a valid choice.'))
        
    # Initializing the value of choice_name variable corresponding to the choice value
    if choice == 1 :
        choice_name = 'Rock'
    elif choice == 2 :
        choice_name = 'Paper'
    else :
        choice_name = 'Scissors'
        
    # Print user choice
    print("User's choice is \n",choice_name)
    print("Now computer's turn ...")
    
    # Computer chooses randomly any number among 1, 2 and 3.
    # Using randint method of random module
    comp_choice = random.randint(1,3)
    
    # Looping until comp_choice value is equal to the choice value
    # while comp_choice == choice :
    #     comp_choice = random.randint(1,3)
    
    # Initialize the value of comp_choice_name variable corresponding to the choice value
    if comp_choice == 1 :
        comp_choice_name = 'rock'    
    elif comp_choice == 2 :
        comp_choice_name = 'paper'
    else :
        comp_choice_name = 'scissors'
    
    # Print computer choice
    print("Computer's choice is \n",comp_choice_name)
    print(choice_name,'VS',comp_choice_name)
    
    # Condition for DRAW
    if choice == comp_choice :
        print('It is a DRAW',end="")
        result = 'DRAW'
    
    #Condtion for WIN
    if (choice==1 and comp_choice==2) :
        print('Paper wins =>',end="")
        result = 'paper'
    elif (choice==2 and comp_choice==1) :
        print('Paper wins =>',end="")
        result = 'Paper'
        
    if (choice==2 and comp_choice==3) :
        print('Scissors wins =>',end="")
        result = 'scissors'
    elif (choice==3 and comp_choice==2) :
        print('Scissors wins =>',end="")
        result = 'Scissors'
        
    if (choice==3 and comp_choice==1) :
        print('Rock wins =>',end="")
        result = 'rock'
    elif (choice==1 and comp_choice==3) :
        print('Rock wins =>',end="")
        result = 'Rock'
        
    # Printing either the user or the computer wins or draw
    if result == 'DRAW' :
        print('<== It is a draw ==>')
    if result == choice_name :
        print('<== User wins ==>')
    else :
        print('<== Computer wins ==>')
    
    print("Do you want to play again? (Y/N)")
    # if user input n or N then condition is True
    ans = input().lower
    if ans == 'n' :
        break
    
# After coming out of the while loop we print thanks for playing
print("Thank's for playing!!!")    