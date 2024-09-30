#lab 1 Task Sheet - Guessing game
'''imports: 1'''
import random
'''
criteria:
1. generate random number 
2. allow user to guess
3. give hints, too high/low
Extra additions:
1. attempts recorded
2. start page
'''
'''game function'''
def game():
    '''set up'''
    attempts=0#sets attempts to 0 upon start
    answer=random.randint(1,100)#generates a random number between 1 and 100
    User_guess=""#sets User_guess to empty
    
    '''main game'''
    while answer!=User_guess and attempts<5:#loops till answer and User_guess are the same
        User_guess=int(input("enter a number between 1 and 100: "))#user input for guess
        attempts=attempts+1#adds an attempt
        
        '''checking'''
        if User_guess>answer:#checks if User_guess is larger than the answer
            print("Too High")
        elif User_guess<answer:#checks if User_guess is smaller than the answer
            print("too low")
        elif User_guess == answer:#checks if answer = User_guess
            print("Well done you got the answer in ", attempts, " attempts")
            main()#allows user to play again
        if attempts==5:
            print("you have run out of attempts!")
            main()
              
'''main function'''
def main():
    print("\nwelcome to Guess")
    begin=""#sets begin to empty to start the while loop
    while begin == "":#while loop requiring an input
        begin=input("would you like to begin: ")#askes the user if they want to start(additional Feature)
        if begin == "yes":
            game()#takes the user to the game
        elif begin == "no":
            break

'''calling function'''
main()