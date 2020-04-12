def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
sc = []
for i in range(n):
    sc.append(input())
ob = set(sc)
m = ii()
disc = []
for i in range(m):
    disc.append(input())

score = 0
for i in ob:
    score = max(score,sc.count(i)-disc.count(i))
print(score)