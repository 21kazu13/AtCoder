def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
l = []
for _ in range(n):
    s = input()
    l.append(s[::-1])
#print(l)
l.sort()
#print(l)
for item in l:
    print(item[::-1])