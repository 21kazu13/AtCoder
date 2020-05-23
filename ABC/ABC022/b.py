def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
l = [False]*100001
ans = 0
for _ in range(n):
    kind = ii()
    if l[kind]:
        ans += 1
    else:
        l[kind] = True

print(ans)