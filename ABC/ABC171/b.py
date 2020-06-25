def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

n,k = iim()
P = iil()
P.sort()
print(sum(P[:k]))