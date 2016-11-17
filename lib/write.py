import os

__author__ = "H.D. 'Chip' McCullough IV"


def write_primes(gaussianPrimes):
    print("Writing primes")
    with open(os.path.join(".", "data", "GaussianPrimes.csv"), 'w') as w:
        line = 0
        for i in range(0, len(gaussianPrimes)):
            var = gaussianPrimes[i]
            w.write("{0} + {1}i".format(var[0], var[1]))
            line += 1
            if line == 10:
                w.write('\n')
                line = 0
            else:
                w.write(', ')


def write_probable_primes(probablePrimes):
    with open(os.path.join(".", "data", "ProbablePrimes.csv"), 'w') as w:
        line = 0
        for i in range(0, len(probablePrimes)):
            var = probablePrimes[i]
            w.write("{0} + {1}i".format(var[0], var[1]))
            line += 1
            if line == 10:
                w.write('\n')
                line = 0
            else:
                w.write(', ')
