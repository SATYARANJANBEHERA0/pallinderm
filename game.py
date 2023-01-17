player1 = input("Enter a choice of 1st player(rock, paper, scissors): ")
player2 = input("Enter a choice of 2nd player (rock, paper, scissors): ")


if player1 == player2:
    print("It's a tie!")
elif player1 == "rock":
    if player2 == "scissors":
        print("Rock smashes scissors! player1 win!")
    else:
        print("Paper covers rock! player2 win!.")
elif player1 == "paper":
    if player2 == "rock":
        print("Paper covers rock! player1 win!")
    else:
        print("Scissors cuts paper! player2 win!.")
elif player1 == "scissors":
    if player2 == "paper":
        print("Scissors cuts paper! player1 win!")
    else:
        print("Rock smashes scissors! player2 win.")