import matplotlib.pyplot as py
from random import randint
trials = 1000
outcome = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
for trial in range(trials):
    roll = randint(1,6) + randint(1,6)
    outcome[roll] += 1
py.bar(list(outcome.keys()), outcome.values(), color='g')
py.show()
