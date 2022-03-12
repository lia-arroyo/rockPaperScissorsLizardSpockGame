# Rock Paper Scissors - Fully Working Program Version 3
# Post Usability Testing
# Created: 1/09/18

'''

        v2:
    - Add basic instructions and introduction
        - make sure to include if rock beats scissors, etc

        v3:
    - give users an option to just do rock/paper/scissors 

        v4:
    - make code more efficient
    - fix feedback statements
            - format win/loss statement
            
        v5:
    - make code more efficient
            - convert game rules into list
    
    '''

''' modules '''

import random

''' functions '''
# integer checking function
def intcheck(question, low):

    # set up error messages
        error = "Please enter an integer that is more than or" \
                    " equal to {}".format(low)
        while True:
        
            try:
                response = int(input(question))

                # checks response is not too low
                if low is not None and response < low:
                    print(error)
                    continue

                return response

            except ValueError:
                print(error)
                continue

# STRING CHECKING FUNCTION, to see if user_move is in list (tokens)
def strcheck (question, list):

        # error statement
        error = "Please choose a move from the list given: {}".format(tokens)

        while True:
                try:    
                        response = input(question).lower()

                        # if user_move is not in given tokens
                        if response not in list:
                                print(error)
                                continue
                        
                        return response

                except ValueError:
                        print(error)
                        continue

# feedback statements function
def rps_statement(statement, statement2, statement3, char):
    print()
    print(char*(len(statement)+6))
    print()
    print(statement.center(len(statement)+6))
    print(statement2.center(len(statement)+6))
    print(statement3.center(len(statement)+6))
    print()
    print(char*(len(statement)+6))
 
''' main routine '''

# looping entire game
keep_going = ""
while keep_going == "":

        # token list
        tokens = ["rock", "paper", "scissors"]

        # introduction and instructions

        rps_statement("ROCK PAPER SCISSORS GAME", "Rock, Paper, Scissors", "Lizard, Spock", "#")
        print()
        game_rules = ["Scissors cuts Paper", "Paper covers Rock", "Rock crushes Lizard", "Lizard poisons Spock", "Spock smashes Scissors","Scissors decapitates Lizard","Lizard eats Paper","Paper disproves Spock", "Spock vaporizes Rock", "Rock crushes Scissors"]
        print("Game Mechanics:")
        for item in game_rules: # prints the game rules above ^^^ 
                print(item) 
        print()
        print("Rock/Paper/Scissors/Lizard/Spock was created by Sam Kass.")
        print()
                
        # ASKING USER IF THEY WANT LIZARD AND SPOCK ADDED
        extra = input("Enter N if you want to play with LIZARD and SPOCK or enter any key to play just ROCK/PAPER/SCISSORS ").lower()
        if extra == "n":
                print()
                print("You are playing ROCK/PAPER/SCISSORS/LIZARD/SPOCK")
                print()
                tokens.append("lizard")
                tokens.append("spock")
        else:
                print()
                print("You are playing ROCK/PAPER/SCISSORS")
                print()

        # asks user how many points to win
        first_to = intcheck("How many points to win the game? ", 1) # first_to must be an integer
        print("\n The first to {} points wins the game. \n".format(first_to))
        print("Let's Play! Enter a valid token from the list: {}".format(tokens))
                
        # points counter
        comp_points = 0
        user_points = 0

        # looping rounds until user or computer reaches first_to

        while comp_points < first_to or user_points < first_to:

                # checking the user's move is valid, from the token
                user_move = strcheck("Your move: ", tokens)

                # generating computer's moves
                comp_move = random.choice(tokens)

                # comparing user's move to computer's randomly generated move

                # computer's move is rock
                while comp_move == "rock":
                        
                        if user_move == "rock":
                            user_tie = rps_statement("Computer's move is: {}".format(comp_move.title()), \
                                 "It's a tie!", \
                                "User: {} | Computer: {}".format(user_points, comp_points),"=")
                            print()

                        # user won
                        elif user_move == "paper" or user_move == "spock": # paper covers rock OR spock vaporizes rock
                            user_points += 1
                            user_won = rps_statement("Computer's move is: {}".format(comp_move.title()), \
                                         "You won!!", \
                              "User: {} | Computer: {}".format(user_points, comp_points),"*")
                            print()
                            

                        # user lost
                        elif user_move == "scissors" or user_move == "lizard": #rock crushes scissors or rock crushes lizards
                            comp_points += 1
                            user_lost = rps_statement("Computer's move is: {}".format(comp_move.title()), \
                                  "You lost!", \
                              "User: {} | Computer: {}".format(user_points, comp_points),"~")
                            print()
                        break

                # computer's move is paper
                while comp_move == "paper":

                        if user_move == "paper": #its a tie
                            user_tie = rps_statement("Computer's move is: {}".format(comp_move.title()), \
                                 "It's a tie!", \
                                "User: {} | Computer: {}".format(user_points, comp_points),"=")
                            print()

                        # user won
                        elif user_move == "scissors" or user_move == "lizard": #scissor cuts paper OR lizard eats paper
                            user_points += 1
                            user_won = rps_statement("Computer's move is: {}".format(comp_move.title()), \
                                         "You won!!", \
                              "User: {} | Computer: {}".format(user_points, comp_points),"*")
                            print()

                        # user lost
                        elif user_move == "spock" or user_move == "rock": # paper disproves spock OR paper covers rock
                            comp_points += 1
                            user_lost = rps_statement("Computer's move is: {}".format(comp_move.title()), \
                                  "You lost!", \
                              "User: {} | Computer: {}".format(user_points, comp_points),"~")
                            print()

                        break

                # computer's move is scissors
                while comp_move == "scissors":

                        if user_move == "scissors": # tie
                            user_tie = rps_statement("Computer's move is: {}".format(comp_move.title()), \
                                 "It's a tie!", \
                                "User: {} | Computer: {}".format(user_points, comp_points),"=")
                            print()

                        # user won
                        elif user_move == "rock" or user_move == "spock": #rock crushes scissors OR  spock smashes scissors
                            user_points += 1
                            user_won = rps_statement("Computer's move is: {}".format(comp_move.title()), "You won!!", "User: {} | Computer: {}".format(user_points, comp_points),"*")
                            print()

                        # user lost
                        elif user_move == "paper" or user_move == "lizard": #scissors cuts paper OR scissors decapitates lizard
                            comp_points += 1
                            user_lost = rps_statement("Computer's move is: {}".format(comp_move.title()), \
                                  "You lost!", \
                              "User: {} | Computer: {}".format(user_points, comp_points),"~")
                            print()

                        break

                # computer's move is lizard
                while comp_move == "lizard":
                        if user_move == "lizard": # tie 
                             user_tie = rps_statement("Computer's move is: {}".format(comp_move.title()), \
                                 "It's a tie!", \
                                "User: {} | Computer: {}".format(user_points, comp_points),"=")
                             print()

                        # user won
                        elif user_move == "rock" or user_move == "scissors": #rock crushes lizard OR scissors decapitates lizard
                            user_points += 1
                            user_won = rps_statement("Computer's move is: {}".format(comp_move.title()), \
                                         "You won!!", \
                              "User: {} | Computer: {}".format(user_points, comp_points),"*")
                            print()

                        # user lost
                        elif user_move == "paper" or user_move == "spock": # lizard eats paper OR lizard poisons spock
                            comp_points += 1
                            user_lost = rps_statement("Computer's move is: {}".format(comp_move.title()), \
                                  "You lost!", \
                              "User: {} | Computer: {}".format(user_points, comp_points),"~")
                            print()

                        break

                # computer's move is spock
                while comp_move == "spock":
                        if user_move == "spock":
                            user_tie = rps_statement("Computer's move is: {}".format(comp_move.title()), \
                                 "It's a tie!", \
                                "User: {} | Computer: {}".format(user_points, comp_points),"=")
                            print()

                        # user won
                        elif user_move == "lizard" or user_move == "paper": # lizard poisons spock OR paper disproves spock
                            user_points += 1
                            user_won = rps_statement("Computer's move is: {}".format(comp_move.title()), \
                                         "You won!!", \
                              "User: {} | Computer: {}".format(user_points, comp_points),"*")
                            print()

                        # user lost
                        elif user_move == "scissors" or user_move == "rock": # spock smashes scissors OR spock vaporizes rock
                            comp_points += 1
                            user_lost = rps_statement("Computer's move is: {}".format(comp_move.title()), \
                                  "You lost!", \
                              "User: {} | Computer: {}".format(user_points, comp_points),"~")
                            print()
                        break

                # end game mechanics

                # if user or computer reaches the points needed to win
                if user_points == first_to or comp_points == first_to:
                        print("Game over. ")
                    
                        if user_points == first_to:
                            rps_statement("You are the first to {} points".format(first_to), "Congratulations!", "You won the game!","+")

                        elif comp_points == first_to:
                            rps_statement("Computer was first to {} points.".format(first_to),"You lost. :(", "Sorry!","-")

                        # play again? 
                        keep_going = input("Do you want to play again? Press <enter> to play again or enter any key to quit. ")
                        break
        
