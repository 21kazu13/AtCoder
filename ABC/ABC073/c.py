def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
n = ii()
s = set()
for i in range(n):
    num = ii()
    if num in s:
        s.remove(num)
    else:
        s.add(num)

print(len(s))