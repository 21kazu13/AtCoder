def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
s = list(input())
ans = []
alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

for i in s:
    ans.append(alpha[(alpha.index(i)+n)%26])
print(''.join(ans))