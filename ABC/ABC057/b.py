def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,m = iim()

pe = []
ch = []
for i in range(n):
    pe.append(iil())

for j in range(m):
    ch.append(iil())

for k in pe:
    dist = 1000000000
    point = 0
    for ind,l in enumerate(ch):
        if abs(k[0]-l[0])+abs(k[1]-l[1]) < dist:
            dist = abs(k[0]-l[0])+abs(k[1]-l[1])
            point = ind+1
    print(point)