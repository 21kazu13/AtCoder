import numpy as np
import numba
import time

start_time = time.perf_counter()

@numba.njit
def prime_table(N):
    is_prime = np.zeros(N, np.int64)
    is_prime[2:3] = 1
    is_prime[3::2] = 1
    for p in range(3, N, 2):
        if p * p >= N:
            break
        if is_prime[p]:
            is_prime[p * p::p + p] = 0
    return is_prime, np.where(is_prime)[0]

@numba.njit
def main(N, primes):
    div = np.ones(N + 1, dtype=np.int64)
    for p in primes:
        for i in range(1,N // p + 1):
            div[p * i] += div[i]
    print(div)
    div *= np.arange(N + 1)
    print(div)
    return div.sum()

N = int(input())
is_prime, primes = prime_table(N + 1)
print(main(N, primes))
print("perf_counter = {:.7f}".format(time.perf_counter() - start_time))

