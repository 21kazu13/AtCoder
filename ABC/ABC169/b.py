def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
n = ii()
A = iil()
ans = 1
if 0 in A:
    print(0)
    exit()
for item in A:
    ans *= item
    if ans > 1e18:
        print(-1)
        exit()
print(ans)