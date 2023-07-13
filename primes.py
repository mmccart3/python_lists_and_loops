import time
from math import sqrt
time.perf_counter()

primes_up_to = 100000

#Andrew's solution:
print("############################")
print("### PRIMES CHALLENGE ###")

start = time.perf_counter()
def is_prime(number):
    if (number <= 1): 
        return False 
    for i in range(2,number): 
        if (number % i) == 0: 
            return False 
    return True

# create a list of integers from 2 - 1000
ints = list(range(2, primes_up_to))
# create a new list of prime numbers
primes = [i for i, number in enumerate(ints) if is_prime(number)]

print(f"{len(primes)} primes. ")
finish = time.perf_counter()

elapsed_time = finish - start
print("Andrew's time; ",elapsed_time)

# Mark's solution
start = time.perf_counter()

list_of_primes=[2]

for x in range(2,1000000):
    prime = True
    max = round(sqrt(x),0)
    for y in list_of_primes:
        if y > max:
            break
        if (x % y) == 0:
            prime = False
    if prime:
        list_of_primes.append(x)

print(len(list_of_primes))
finish = time.perf_counter()

elapsed_time = finish - start
print("Mark's elapsed time: ",elapsed_time)