import random

class guessNo:
    @staticmethod
    def start_game():
        print("Welcome to the Number Guessing Game!")
        
        # Generate a random number between 100 and 200
        randomNumber = random.randint(100 , 200)
        attempts = 0

        while True:
            userNo = int("enter the number : ")
            attempts += 1
            
            if userNo < randomNumber:
                print("you enter the low no ! plese guess the aqurate no ")
            elif userNo > randomNumber :
                  print("you enter the high no ! plese guess the aqurate no ")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
    start_game() 