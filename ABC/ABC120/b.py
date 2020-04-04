def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

a,b,k = iim()
ans = []
for i in range(1,min(a,b)+1):
    if a%i == 0 and b%i == 0:
        ans.append(i)

print(ans[-k])