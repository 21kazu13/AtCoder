n = int(input())
A = list(map(int,input().split()))

A.sort(reverse=True)
alice = 0
bob = 0

for i in range(0,n):
    if i%2==0:
        alice = alice + A[i]
    else:
        bob = bob + A[i]
print(alice - bob)