
while True:
    player1 = input("Player 1, please choose your weapon: \n1 = Rock\n2 = Paper\n3 = Scissors\n")
    player2 = input("Player 2, please choose your weapon:  \n1 = Rock\n2 = Paper\n3 = Scissors\n")

    if player1 == "Rock" and player2 == "Paper" or player1 == "Paper" and player2 == "Scissors" or player1 == "Scissors" and player2 == "Rock":
        print("player2 wins")
    else:
        print("player1 wins")
    next_round = input("Do you want to play another round?")
    if next_round != "yes":
        break


    
