def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
n = ii()
A = iil()
ans = 0
for i in range(n):
    hmax = 0
    hmaxindex = 0
    for j in range(n):
        if A[j]:
            if hmax <= A[j]*abs(i-j):
                hmax = A[j]*abs(i-j)
                hmaxindex = j
    A[hmaxindex] = False
    ans += hmax
    print(i,hmaxindex,hmax)
print(ans)
