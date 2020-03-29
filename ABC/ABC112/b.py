def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,T = iim()
cost = 1001
for i in range(n):
    c,t = iim()
    if t <= T:
        cost = min(cost,c)
if cost == 1001:
    print('TLE')
else:
    print(cost)
