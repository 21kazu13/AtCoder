def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,m = iim()
bonus = {}

for i in range(n):
    a,b = iim()
    bonus[a] = max(bonus.get(a,0),b)

print(bonus)