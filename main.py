from distutils.version import LooseVersion
import random
from unicodedata import name
from art import vs 
from art import logo
from game import data

game_end =False

while  game_end:
    print(logo)

    compare_A = random.choice(data)
    
    print(f"Compare A: {compare_A['name']} a {compare_A['description']} from {compare_A['country']}.")

    print(vs)

    Against_B = random.choice(data)
    
    print(f"Compare A: {Against_B['name']} a {Against_B['description']} from {Against_B['country']}.")


    def guess (guess):

        if guess == 'A' :
                return compare_A
        else:
        
                return Against_B

    guess_1 = guess(guess = input("Who has more followers? Type 'A' or 'B' : "))


    def compare (guess_1):
        
        if guess_1["follower_count"] == compare_A["follower_count"] :
            print("You win")
            return 1
        elif guess_1["follower_count"] < compare_A["follower_count"] :
            print("You loss")
            return 0

    count = compare(guess_1)


    score = 0
    if count == 1:
        score += 1
    else:
        print("You loss " )
        print (f"Your score is {score}")
        game_end =True


         
        


