def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,m = iim()
l = set(range(1,m+1))

for i in range(n):
    A = set(iil()[1:])
    l = l&A

print(len(l))