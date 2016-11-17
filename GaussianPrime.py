import sys
import lib.prime
import lib.write

__author__ = "H.D. 'Chip' McCullough IV"


if __name__ == "__main__":
    sieve = lib.prime.sieve_of_eratosthenes()
    end = int(sys.argv[1])
    gp = []
    prb = []
    for re in range(0, end+1):
        print("re = {0}".format(re))
        for im in range(0, end+1):
            if re == 0:                                                        # CASE: z = 0 + iB
                if im <= 100000:                                                   # CASE: B <= 100,000
                    if im in sieve:                                                    # Use Sieve of Eratosthenes
                        if (im % 4) == 3:                                                  # |B| := 3 ( mod 4)
                            gp.append((re, im))                                                # Append z = (0, B)
                    else:                                                          # CASE: B > 100,000
                        if lib.prime.probable_prime(im) and (im % 4) == 3:             # B probable? & |B| := 3 ( mod 4)
                            prb.append((re, im))                                           # Append prbz = (0, B)
            elif im == 0:                                                      # CASE: z = A + i0
                if re <= 100000:                                                   # CASE: A <= 100,000
                    if re in sieve:                                                    # Use Sieve of Eratosthenes
                        if (re % 4) == 3:                                                  # |A| := 3 ( mod 4)
                            gp.append((re, im))                                                # Append z = (A, 0)
                    else:                                                          # CASE: A > 100,000
                        if lib.prime.probable_prime(re) and (re % 4) == 3:             # A probable? & |A| := 3 ( mod 4)
                            prb.append((re, im))                                           # Append prbz = (A, 0)
            else:                                                              # CASE: z = A + iB
                norm = pow(re, 2) + pow(im, 2)                                     # Calculate |z|
                if norm <= 100000:                                                 # CASE: |z| <= 100000
                    if norm in sieve:                                                  # Use Sieve of Eratosthenes
                        gp.append((re, im))                                                # Append z = (A, B)
                    else:                                                          # CASE: |z| > 100000
                        if lib.prime.probable_prime(norm):                              # |z| is probable prime?
                            prb.append((re, im))                                            # Append prbz = (A, B)
    lib.write.write_primes(gp)
    lib.write.write_probable_primes(prb)
