import math

# the following function returns all prime numbers in the range 1 to n
def seive(n):
  # declare a list of n + 1 numbers
  # primes[k] == 1 means the number is prime
  # primes[k] == 0 means the number is not prime
  primes = [1] * (n + 1)

  # print primes

  for i in xrange(2, int(math.sqrt(n+1))): # since 1 is not a prime number
    # find multiples of i and remove from primes
    m = 2
    while i * m <= n: # i = 2, m = 2 => 4 in n
      primes[i * m] = 0
      m += 1

  # print primes

  for i, p in enumerate(primes):
    if i == 0 or i == 1:
      continue

    if primes[i] == 1:
      print i

seive(20)
