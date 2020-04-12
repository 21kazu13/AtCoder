def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
A = iil()
cnt = 0

for i in A:
    while i%2 == 0:
        cnt += 1
        i //= 2

print(cnt)