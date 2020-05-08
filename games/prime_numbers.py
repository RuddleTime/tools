"""
Accepts in int from command line.
Generates list of all prime numbers up to that number.
"""

import argparse
import math


def get_prime_numbers(number):
    """
    Generates prime numbers

    :param number: Number up to which prime numbers should be produced
    :returns: list of prime numbers
    :rtype: list
    """
    prime_numbers = []
    i=0
    while i<number:
        for x in range(2, int(math.sqrt(i)+1)):
            if i%x==0:
                break
        else:   
            prime_numbers.append(i)
        i+=1
    return prime_numbers


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", type=int, help="number to get primes of")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    number = args.number
    print(get_prime_numbers(number))
