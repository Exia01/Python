# Write a function called next_prime, which returns a generator that will yield an unlimited number of primes, starting from the rst prime
# (2).
# Recall that a prime number is any whole number that has exactly two divisors: one and the number itself. The rst few primes are 2, 3, 5,
# 7, 11, ... .


def next_prime():
      # instantiating variables
    i = 0
    while True:  #alway running
        print(i)
        i+=1
        if(i//1 ==i and i%2==1):
            yield i

        


# Test Cases
primes = next_prime()
x = (next(primes) for i in range(5))
print(list(x))

