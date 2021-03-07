import random

def user_prompt(prompt, default=None):
    "Allow use of default values in input."
    prompt = '{}[{}]:'.format(prompt, default)
    response = input(prompt)
    if not response and default:
        return default
    else:
        return response 

num_runs = int(user_prompt("Input number of runs", "20000"))

    #ways to win

first_choice_wins = 0
switch_doors_wins = 0
doors = ['a', 'b', 'c']

for i in range(num_runs):
    winner = random.choice(doors)
    pick = random.choice(doors)
    if winner == pick:
        first_choice_wins += 1
    else: 
        switch_doors_wins += 1
    
print("wins with first pick ={}".format(first_choice_wins))
print("Wins with switched pick ={}".format(switch_doors_wins))
print("probability of winning with initial guess:{:.2f}".format(first_choice_wins / num_runs))
print("probability of winning with switched guess:{:.2f}".format(switch_doors_wins / num_runs))

input("\nPress the Enter key to exit.")