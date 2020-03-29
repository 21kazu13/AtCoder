import math
def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
l = []
for i in range(n):
    l.append(iil())

dist = 0

for item in l:
    for comp in l:
        dist = max(dist,math.sqrt((item[0]-comp[0])**2+(item[1]-comp[1])**2))

print(dist)