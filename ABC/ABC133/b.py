def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,d = iim()
cd = []
for i in range(n):
    cd.append(iil())
cnt = 0
for i in range(n):
    for j in range(i+1,n):
        di = sum([(y-x)**2 for (x,y) in zip(cd[i],cd[j])])**0.5
        if di == int(di):
            cnt += 1

print(cnt)