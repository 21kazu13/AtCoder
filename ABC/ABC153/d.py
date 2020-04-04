def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

h = ii()
count = 0
ans = 1
while h >= 2:
    h = h//2
    ans += 2*count
    count += 1
#print(ans,count)
if count == 0:
    print(1)
else:
    print(2**(count+1)-1)
