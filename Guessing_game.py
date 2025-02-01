import random

def guessing_game():
    
    secret_number = random.randint(1, 10)
    attempts = 0

    print("I'm thinking of a number between 1 and 10.")

    while True:
        try:
            
            guess = input("Take a guess between number 1-10: ")

            
            if not guess.isdigit():
                print("Invalid input. Kindly enter a valid number.")
                continue

            guess = int(guess)

            
            if guess < 1 or guess > 10:
                print("Please guess a number between 1 and 10.")
                continue

            attempts += 1

            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Bravo! You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

    
    play_again = input("Wanna play again? (y/n): ").lower()
    return play_again == 'y'

if __name__ == "__main__":
    while True:
        
        if not guessing_game():
            print("Thanks for playing! Later!")
            break
