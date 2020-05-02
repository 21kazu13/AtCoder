def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

s = input()
k = int(input())
l = []
if len(s) >= k:
    for i in range(len(s)-k+1):
        l.append(s[i:i+k])
    print(len(set(l)))
else:
    print(0)
