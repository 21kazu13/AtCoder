def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
n = ii()
A = iil()
ans = [0]*n
for i,item in enumerate(A):
    ans[item-1] = i+1

for i in ans:
    print(i,end=' ')