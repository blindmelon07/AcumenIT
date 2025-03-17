import random

heroes = [
    "SUperman", #0
    "Saitama",  #1
    "Deku",     #2
    "Ironman",  #3
    "Gagamboy", #4
    "Darna",    #5
    
]

best = random.choice(heroes)
power = random.randint(9000, 10000)


template = "The best hero is {} with a power level of {}."
output = template.format(best, power)
print(output)