#imports
import random
'''single round'''
def play_single_round():
    random_number=random.randint(1,100)#generates random number
    attempts=0#resets attempts to 0
    max_attempts=10#sets max_attempts
    guess=None#voids guess
    print("you have, ", max_attempts, " attempts left")#number of attempts lefts
    while guess!=random_number and attempts<=max_attempts:
        try:
            guess=int(input("enter a number in digit form 1-100: "))#guess input
        except ValueError:#checks if a value error message triggered avoiding it
            print("please enter a valid number")
        if guess<random_number:#checks if guess is too low
            print("too low")
            attempts+=1#adds attempt
            print("you have used up ", attempts, " out of ", max_attempts, " attempts")#prints attempts used up
        elif guess>random_number:#checks if guess is too high
            print("too high")
            attempts+=1#adds attempt
            print("you have used up ", attempts, " out of ", max_attempts, " attempts")#prints attempts used up
        elif attempts==max_attempts:#checks if attempts ran out
            print("you have run out of attempts, the correct number was", random_number)#prints fail message with answer
            return max_attempts-attempts#returns score
        else:
            print("well done, you got the answer in ", attempts, " attempts")#prints correct message with attempts taken
            return max_attempts-attempts#returns score

def play_game():
    total_rounds=3#sets total number of rounds
    total_score=0#reset score to 0 on original run
    i=1#sets iteration
    print("welcome to guess")#welcome message
    for i in range(total_rounds):#loop 3 times
        print("round ", i)#prints round number
        score=play_single_round()#calls play_single_round function as stores returned value as score
        total_score+=score#adds round score to total score
        print("that round you scored ", score)#displays points
        i+=1#iterates to next round
    if i==total_rounds:#checks if number of iterations is complete
        if total_score<=10:#checks total score
            print("poor, ", total_score, " that an average score of ", total_score/3, " per round")#prints result
        elif 10<total_score<=20:##checks total score
            print("better look next time, ", total_score, " that an average score of ", total_score/3, " per round")#print result
        elif 20<total_score<=30:#checks total score
            print("amazing, ", total_score, " that an average score of ", total_score/3, " per round")#print result

if __name__=="__main__":#main guard
    play_game()#calls function to begin the game

        



#attempts+=1