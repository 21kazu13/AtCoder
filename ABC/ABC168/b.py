def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
k = ii()
s = input()

if len(s) <= k:
    print(s)
else:
    print(s[:k]+'...')