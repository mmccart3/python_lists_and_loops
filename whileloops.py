import random

rand_num = random.randint(0,50)
print (rand_num)
my_num = 37
counter = 1

while rand_num != my_num:
    rand_num = random.randint(0,50)
    counter += 1
    print(counter, rand_num)

# index = 0

# while index < 10:
#     print (index)
#     index = index + 1
# #   index += 1 
