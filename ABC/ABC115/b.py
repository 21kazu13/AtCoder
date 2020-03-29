def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
prices = []
for i in range(n):
    prices.append(ii())

print(sum(prices)-max(prices)//2)