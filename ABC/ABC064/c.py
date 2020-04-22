def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
A = iil()

l = [0]*9
for i in A:
    l[min(i//400,8)] += 1

lf = l[:-1]
ans = 8-lf.count(0)
print(max(1,ans),ans+l[8])
