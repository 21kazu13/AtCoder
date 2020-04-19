def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

N = sorted(iil(),reverse=True)
ans = N[0]-N[1]
#print(ans)
if (N[0]-N[2]-ans)%2 == 0:
    ans += (N[0]-N[2]-ans)//2
else:
    ans += (N[0]-N[2]-ans)//2 + 2


print(ans)