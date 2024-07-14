def play_game():
    import random

    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    difficulty = 0
    if difficulty_level == "easy":
        difficulty = 10
        print("You will get 10 attempts")
    elif difficulty_level == "hard":
        difficulty = 5
        print("You will get 5 attempts")
    else:
        print("invalid input")

    computer_number = random.randint(0, 100)
    user_number = int(input("Guess a value between 0 to 100: "))
    if user_number == computer_number:
        print("Your Guess is correct")
    elif user_number > computer_number:
        print("Too High\n")
    else:
        print("Too Low\n")
    print(f"You have {difficulty - 1} attempts left")

    for i in range(difficulty - 1):
        user_number = int(input("Guess Again: "))
        if user_number == computer_number:
            print("Your Guess is correct")
            break
        elif user_number > computer_number:
            print("Too High\n")
        else:
            print("Too Low\n")
        print(f"You have {difficulty - 2 - i} attemps left")


Lets_play = True
while Lets_play:
    play_game()
    continuation = input("Do you want to play again? 'y', 'n': ")
    if continuation == 'n':
        Lets_play = False
