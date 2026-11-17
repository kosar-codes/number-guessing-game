import random
max_attempts=10
secret_number=random.randint(1, 100)
attempts=0

def show_welcome():
    print("------------")
    print("welcome to the Number Guessing Game!")
    print("The rules of the game are that you guess the number")
    print("if it is the same as the computer's number, you win")
    print("and if it is not the same, you have to keep guessing to win")
    print("The guesses are between numbers 0 and 100.")
    print("Ready, hero??? Let's goooo!")
    print("------------")
    print("Choose your level: Easy (e) or Hard (h)")
    
show_welcome()

level = input("Enter your choice (e/h): ")
if level=="e":
    max_attempts = 10
    secret_number=random.randint(1, 50)
       
elif level == "h":
    max_attempts=5
    secret_number=random.randint(1, 100)
    
else:
    print("invalid levelDefaulting to Hard.")
    max_attempts=5
    secret_number=random.randint(1, 100)

def finish():
    print("--- Game Over! Thanks for playing! --- ")

while True:          
    attempts=0 
    if level == "e":
        secret_number = random.randint(1, 50)
    else:
        secret_number = random.randint(1, 100)
        
    while attempts < max_attempts:
        user_guess=int(input("enter your guess?????:"))
        attempts = attempts + 1
        
        if user_guess== secret_number:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            finish()
            break
        
        elif user_guess > secret_number :
            print("My number is smaller. Try again")
            
        else:
            print("My number is bigger.Try again")
            
    if attempts==max_attempts:
        print(f"Game over! You lost. The correct number was {secret_number} ")
            
    playing_again=str(input("Do you want to play again??(Y/N):"))
    if playing_again!="Y":
        print("^Thanks for playing^ Goodbye...")
        break
    
