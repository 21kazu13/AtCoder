import math
def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
cd = []
for i in range(n):
    cd.append(iil())

dist = 0
for i in range(n):
    for j in range(i,n):
        dist += math.factorial(n-1)*2*((cd[i][0]-cd[j][0])**2+(cd[i][1]-cd[j][1])**2)**0.5
print(dist/math.factorial(n))