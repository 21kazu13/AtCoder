def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

n = ii()
A = iil()
mirror = 0
for i in A:
    mirror = mirror^i

print(*map(lambda x:x^mirror,A))