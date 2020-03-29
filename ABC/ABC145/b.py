def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
n = ii()
s = input()
if n%2 != 0 or s[:len(s)//2] != s[len(s)//2:]:
    print('No')
else:
    print('Yes')