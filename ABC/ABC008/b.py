def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
d = {}

for i in range(n):
    s = input()
    d[s] = d.get(s,0) + 1
#print(d)
print(max(d, key=d.get))