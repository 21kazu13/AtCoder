def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

n = ii()
A = sorted(iil(),reverse=True)
print(sum(A[::2]))
