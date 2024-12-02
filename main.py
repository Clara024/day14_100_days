from getpass import getpass as input
print ("Epic Rock, Paper, Scissors Battle")
R = 'Rock'
P = 'Paper'
S = 'Scissor'
print ("Select your moves: R,P,S?")
player_1= input("What is your move?")
player_2= input("What is your move?")

if player_1 == "R" and player_2 == "P":
  print()
  print("Player2 wins by smothering player1's rock with paper!")
elif player_1 == "R" and player_2 == "S":
  print()
  print("Player1 wins by blunting player2 scissors with a rock!")
elif player_1 == "P" and player_2 == "R":
  print()
  print("Player1 wins by covering player2's rock with paper!")
elif player_1 == "P" and player_2 == "S":
  print()
  print("Player2 wins by cutting up player1 paper with scissors!")
elif player_1 == "S" and player_2 == "R":
  print()
  print("Player2 wins byblunting player1's scissors with his rock!")
elif player_1 == "S" and player_2 == "P":
  print()
  print("Player1 wins by cutting player1's paper with a mighthy scissors!")
elif player_1 == player_2:
  print()
  print("It's a tie!")
  print("You have to go again!")
else:
  print()
  print("Invalid input.")