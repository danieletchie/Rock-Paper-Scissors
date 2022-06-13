import random


choices = {
    "R": "Rock",
    "P": "Paper",
    "S": "Scissors"
}
is_invalid = True
print("Welcome to CM Rock, Paper, Scissors game")
while is_invalid:
    player = input("Please Type 'R' for rock, 'P' for paper and 'S' for scissors:  ").capitalize()
    if player not in choices.keys():
        print("\nYou typed the wrong input read the instructions carefully \n")
        continue
    player_choice = choices[player]
    computer = random.choice(list(choices.values()))
    print(f"Player: ({player_choice}),  CPU ({computer})")
    if player_choice == computer:
        print("There is a tie")
        print("You have to choose again")
        continue
    elif player_choice == "Paper":
        if computer == "Rock":
            print("The winner is: Player")
        elif computer == "Scissors":
            print("The winner is: CPU")
    elif player_choice == "Rock":
        if computer == "Paper":
            print("The winner is: CPU")
        elif computer == "Scissors":
            print("The winner is: Player")
    elif player_choice == "Scissors":
        if computer == "Paper":
            print("The winner is: CPU")
        elif computer == "Rock":
            print("The winner is: Player")
    break
    