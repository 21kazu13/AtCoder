def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

price = []
n = ii()
for i in range(n):
    price.append(ii())

ans = sorted(list(set(price)),reverse=True)
print(ans[1])