__author__ = "H.D. 'Chip' McCullough IV"


def sieve_of_eratosthenes():
    """
    Sieve of Eratosthenes method of finding a prime number. This is a one shot algorithm that returns primes from
    2-100000. When a composite number is found, it is removed from the sieve, which speeds up runtime as the program
    continues. After this, a better method needs to be employed to find primes.
    :return: list of length 9592
    """
    sieve = list(range(2, 100001))
    for i in sieve:
        for j in sieve:
            if i != j:
                if (j % i) == 0:
                    sieve.remove(j)
    return sieve


def probable_prime(num):
    """
    Determines if the passed number, param:num, is a probable prime using Fermat's test for completeness. While this
    does not ensure param:num is a prime, (param:num may be a pseudoprime)
    :param num: integer number > 100000
    :type num: int
    :return: bool
    """
    fermat = False
    if num - 1 >= 0:
        fermat = pow(2, num - 1, num) == 1
    return fermat
