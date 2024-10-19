# snake paper scissors

# permission for user
def asking():
    print("Do you want to play the Game ! type (yes/no).")
    userIntres = input().lower()
    if userIntres == 'yes':
        gamestart()
    else:
        print("Thank you! You are not interested in the game.")


# game start
def gamestart():
    import random
    print("Welcome to the Snake, Paper, Scissors game!")
    print("Rules: \n1. Snake beats Paper. \n2. Paper beats Scissors. \n3. Scissors beats Snake.")
    
    # Ask user for a valid choice
    userChoice = input("Choose your option (snake/paper/scissors): ").lower()
    while userChoice not in ['snake', 'paper', 'scissors']:
        userChoice = input("Invalid choice! Please choose again (snake/paper/scissors): ").lower()
    
    computerChoice = random.choice(['snake', 'paper', 'scissors'])
    print("Computer chose: ", computerChoice)
    
    # result
    if userChoice == computerChoice:
        print("It's a tie!")
        print(computerChoice)
    elif (userChoice == 'snake' and computerChoice == 'paper') or \
         (userChoice == 'paper' and computerChoice == 'scissors') or \
         (userChoice == 'scissors' and computerChoice == 'snake'):
        print("You win the game !")
    else:
        print("You lose the game !")
    
    # replay
    print("Do you want to play again? (yes/no)")
    userReplay = input().lower()
    if userReplay == 'yes':
        gamestart()
    else:
        print("Thank you for playing!")
asking()