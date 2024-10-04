import random


def get_choices():
  player_choice = input("Enter your choice (rock, paper or scissors)")
  rand = random.randint(0, 2)
  arr = ["rock", "paper", "scissors"]

  return [player_choice, arr[rand]]


def check_win(player_choice, computer_choice):


  # SAME CHOICE
  if player_choice == computer_choice:
    answer = "there was a tie"
  # ROCK CONDITIONAL
  elif player_choice == "rock":
    if computer_choice == "paper":
      answer = "computer won this round: paper kills rock"
    elif computer_choice == "scissors":
      answer = "you won this round: rock kills scissors"

      # PAPER CONDITIONAL
  elif player_choice == "paper":
    if computer_choice == "rock":
      answer = "you won this round: paper kills rock"
    elif computer_choice == "scissors":
      answer = "computer won this round: Scissors kill paper"

      # SCISSORS CONDITIONAL
  elif player_choice == "scissors":
    if computer_choice == "paper":
      answer = "you won this round: scissors kill paper"
    if computer_choice == "rock":
      answer = "computer won this round: rock kills scissors"

  return answer


def rock_paper_scissor_game():
  gameStatus = "yes"

  while gameStatus == "yes":
    choices = get_choices()
    player_choice = choices[0]
    computer_choice = choices[1]
    answer = check_win(player_choice, computer_choice)

    print("computer choice was: " + computer_choice)
    print("your choice was:     " + player_choice)
    print("______________________________________")
    print(answer)

    print("______________________________________")
    print("______________________________________")
    gameStatus = input("would you like to continue the game? (Yes/No)").lower()

  return


print(rock_paper_scissor_game())
