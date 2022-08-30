import imp
from art import logo
from art import vs
import random
from game import data

score = 0

def format_data(account):
    """from the account data into printable format"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    print(f"{account_name},a {account_desc},from{account_country}")



def check_answer(guess,a_followers,b_followers):
    
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"





    #Display
print(logo)
game_should_continue = True
account_b = random.choice(data)

    #Generate a random account from the game data

while game_should_continue:

    
    account_a =random.choice(data)
    account_b = random.choice(data)

    while account_a == account_b:
       account_b = random.choice(data)

      

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")


    guess = input("Who has more followers? Type 'A' or 'B'")

    a_follower_count = account_a["follower-count"]
    b_follower_count = account_b["follower-count"]
    is_correct =check_answer(guess, a_follower_count, b_follower_count)


    #score keeping

    if is_correct:
        score += 1
        print(f"You're right! current score {score}")
    else:
        print(f"Sorry, thats wrong! Current score {score}")
        game_should_continue =False



 

