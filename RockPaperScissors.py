import random
choices=['rock','paper','scissors']
user_won=0
computer_won=0
draw=0

print("<<< Welcome to Rock Paper Scissors >>>")

while True:

    user_choice=input("Enter your choice(rock / paper /scissors): ").lower()
    
    if user_choice in choices:
        print("You chose ",user_choice)
        computer_choice=random.choice(choices)
        print('Computer chose ',computer_choice)
        if user_choice==computer_choice:
            print("It's a draw !")
            draw+=1
        elif (user_choice=='rock' and computer_choice=='paper') or (user_choice=='paper' and computer_choice=='scissors')or (user_choice=='scissors' and computer_choice=='rock'):
            print("computer won!")
            computer_won+=1
        else:
            print("You won!")
            user_won+=1
        while True:
            signal=input("want to play again? Enter (y/n)...").lower()
            if signal=='n' or signal=='y':
                break
            else:
                print("Please enter y or n")
        if signal=='n':
            break
    
    else:
        print("invalid choice! Please enter(rock , paper or scissors)")       
    
print("you won",user_won,"times")
print("computer won",computer_won,"times")
print("drawn matches are ",draw)