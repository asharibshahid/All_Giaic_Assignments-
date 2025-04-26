import random 

def simulate():
    for i in range(1,3):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f"Roll {i}: Dice 1 = {dice1}, Dice 2 = {dice2}")

simulate()
