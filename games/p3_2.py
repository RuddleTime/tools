"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def prime(number_to_test):
    half_number = int(number_to_test/2)
    factors = get_factors(number_to_test)
    print("Factors of {0}: {1}".format(number_to_test, factors))
    prime_factors = get_prime_factors(factors)
    print("Prime factors of {0}: {1}".format(number_to_test, prime_factors))

def get_factors(number):
    factors = []
    for i in range(3, int(number/2)):
        if number % i == 0:
            factors.append(i)
    return factors

def get_pfactors(number):
    factors = []
    for i in range(2, int(number/2)):
        if number % i == 0:
            factors.append(i)
            break
    return factors


def get_prime_factors(factors):
    prime_factors = []
    for i in factors:
        if len(get_pfactors(i)) == 0:
            prime_factors.append(i) 
    return prime_factors


if __name__ == '__main__':
    prime(13195)
    prime(6008514)
    prime(600851475143)
