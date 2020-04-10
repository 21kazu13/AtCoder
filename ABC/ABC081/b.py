def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
A = iil()

ans = 30

for i in A:
    num = i
    count = 0
    while num%2 == 0:
        num //=2
        count += 1
    ans = min(ans,count)

print(ans)