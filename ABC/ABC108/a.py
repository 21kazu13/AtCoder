def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

k = ii()
even = k//2
if k%2 == 0:
    odd = k//2
else:
    odd = k//2+1

print(even*odd)