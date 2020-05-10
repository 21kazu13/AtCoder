def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
n = ii()
l = []
for _ in range(n):
    l.append(ii())

l.sort(reverse=True)

gr1 = 0
gr2 = 0

for item in l:
    if gr1 <= gr2:
        gr1 += item
    else:
        gr2 += item
print(max(gr1,gr2))