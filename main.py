__author__ = 'saimanoj'

import eratosthenes


def main():
    primes = list(eratosthenes.sieve(100000000))
    print len(primes)


if __name__ == "__main__":
    main()

