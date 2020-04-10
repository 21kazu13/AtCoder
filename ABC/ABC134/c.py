def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
A = []
for i in range(n):
    A.append(ii())

amax = max(A)
anmax = sorted(A)[-2]
cntmax = A.count(amax)

if cntmax > 1:
    for j in A:
        print(amax)
else:
    for k in A:
        if k == amax:
            print(anmax)
        else:
            print(amax)