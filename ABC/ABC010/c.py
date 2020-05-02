def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

w,x,y,z,t,v = iim()
start = (w,x)
end = (y,z)
flag = False

n = ii()

for i in range(n):
    x,y = iim()
    dist = ((start[0]-x)**2 + (start[1]-y)**2)**0.5+((end[0]-x)**2 + (end[1]-y)**2)**0.5
#    print(dist)
    if dist <= t*v:
        flag = True
print('YES' if flag else 'NO')