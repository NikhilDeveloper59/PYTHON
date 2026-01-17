# Used for random numbers / selections.
import random

print(random.randint(1,50)) # this will choose any random number between 1 to 50

print(random.choice(['A','B','C'])) # this will choose any value from given input

l = [1,2,3,4,5,6,7]
random.shuffle(l) # suffle element of list rondomlly
print(l)