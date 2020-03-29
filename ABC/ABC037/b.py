def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,q = iim()
A = [0]*n

for i in range(q):
    l,r,t = iim()
    for j in range(l,r+1):
        A[j-1] = t
for item in A:
    print(item)