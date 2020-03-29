def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
n = ii()
if 1<=n%40<=20:
    if (n%40)%20 != 0:
        print((n%40)%20)
    else:
        print(20)
else:
    if (n%40)%20 != 0:
        print(21-(n%40)%20)
    else:
        print(1)
