# 1) Import the random function and generate both a random number between 0 and 1 as well as a random number between 1 and 10.

# 2) Use the datetime library together with the random number to generate a random, unique value.

from random import random
from datetime import time

num_between_0_and_1 = random()
num_between_1_and_10 = random() * 10


print()