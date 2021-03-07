# example of repeated random sampling which I'll use again in the Monte Carlo simulation. 

import random
from random import randint
trials = 5000000
success = 0
for trial in range(trials):
    faces = set()
    for rolls in range(6):
        roll = randint(1,6)
        faces.add(roll)
    if len(faces) == 6:
        success += 1
print("probability of success = {}".format(success/trials))