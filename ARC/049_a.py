def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

s = list(input())
a,b,c,d = iim()

s.insert(a,'"')
s.insert(b+1,'"')
s.insert(c+2,'"')
s.insert(d+3,'"')
print(''.join(s))