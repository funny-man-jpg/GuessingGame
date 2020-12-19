import random

def run(minNum=1, maxNum=1000, maxAttempts=5):
    def main():
        keepPlaying = True
        while keepPlaying:
            answer = random.randint(1,1000)
            showWelcome()
            handleGuesses(answer)



def promptForNumber():
    """Asks the user to guess a number

    Returns
    -------
    int
        The user input converted to an integer

    """
    return int(input("\nPick a number between 1 and 1000"))

def showWelcome():
    print("Welcome to the Guessing Game.")
    print("The object of the game is to guess a number between 1 and 1000 withing 5 tries")

def promptKeepPlaying():
    """Asks the player (y/n) if they want to keep playing

    If the user enters "y", we return True, if "n", we return False

    Returns
    -------
    bool
        True if player wants to play again, False otherwise.


    """

    correctInput = False
    while not correctInput:
        ans = input("Do you want to play again? (y/n)")
        if ans == 'y':
            return True
        elif ans == 'n':
            return False


def handleGuesses(answer):
    attempts = 0
    while attempts < 5:
        try:
            guess = promptForNumber()
            if guess < answer:
                 print("bigger")
            elif guess > answer:
                 print("smaller")
            else:
                print("correct!")
                return
        except ValueError:
            print(f"You didn't enter an integer. Please try again")
        except:
            print("I didn't understand that. Please try again.")
        else:
            attempts += 1
    else:
        print(f"Sorry you've run out of attempts. The answer is {answer}")


    