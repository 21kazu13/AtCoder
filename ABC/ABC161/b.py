def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
n,m = iim()
A = sorted(iil(),reverse=True)

if A[m-1]*4*m >= sum(A):
    print('Yes')
else:
    print('No')