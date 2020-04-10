def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,m = iim()
l = [0]*n

for i in range(m):
    a,b = iim()
    l[a-1] += 1
    l[b-1] += 1
for j in l:
    print(j)