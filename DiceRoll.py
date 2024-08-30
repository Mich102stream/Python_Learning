# Simple Dice Rolling Script


import random

min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices...")
    print("The values are....")
    print(random.randint(min, max))
    #print(random.randint(min, max))

    roll_again = input("Roll the dices again?")
    
# The above script is a simple dice rolling script that generates two random numbers between 1 and 6 and prints them out.

# The script uses the random.randint() method to generate random numbers between 1 and 6.


# Simple crit chance script using the random module in a dice style roll

import random

hit_chance =  random.randint(1, 6)

print(hit_chance)
if hit_chance == 6:
    print("Critical Hit!")
elif hit_chance >= 3:
    print("Hit!")
else:
    print("Miss!")
    
