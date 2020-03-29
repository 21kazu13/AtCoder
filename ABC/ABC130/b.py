def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,x = iim()
L = iil()
ans = 1
dis = 0
for item in L:
    dis += item
    if dis <= x:
        ans += 1
    else:
        break
print(ans)