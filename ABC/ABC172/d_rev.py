def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
import numba
import time

start_time = time.perf_counter()


@numba.njit
def sieve_of_erastosthenes(num):
    input_list = [False if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 else True for i in range(num)]
    input_list[0] = input_list[1] = False
    input_list[2] = input_list[3] = input_list[5] = True
    sqrt = num**0.5

    for serial in range(3, num, 2):
        if serial >= sqrt:
            prime_list = [i for i, b in enumerate(input_list) if b == True]
            return prime_list

        for s in range(serial ** 2, num, serial):
            input_list[s] = False

@numba.njit
def solve(n):
    ans = 1
    l = sieve_of_erastosthenes(n+1)
    for i in range(2,n+1):
        num = i
        fac = 1
        for j in l:
            cnt = 1
            while num%j==0:
                num //= j
                cnt +=1
            fac *= cnt
            if num == 1:
                break
        ans += i*fac
    return ans

n = ii()
print(solve(n))
print("perf_counter = {:.7f}".format(time.perf_counter() - start_time))
