import os
import statistics
import math
import string
import random

# os module
current_work_dir=os.getcwd()
print(current_work_dir)
# os.mkdir("New Project")

# statistics module
ages=[56,20,56,64,33,87,13,45]
print(statistics.mean(ages))
print(statistics.median(ages))

# math module
print(math.pi)
x=math.pow(2,3)
print(int(x))

# string module
print(string.digits)
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)

# random module
random_num=random.randint(1,10)
print(random_num)