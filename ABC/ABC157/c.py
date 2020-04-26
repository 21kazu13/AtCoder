def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,m = iim()
l = [-1]*n
flag = True
for i in range(m):
    s,c = iim()
    if l[s-1] != -1 and l[s-1] != c:
        flag = False
    else:
        l[s-1] = c

if n > 1 and l[0] == 0:
    flag = False

ans = ''
for i,item in enumerate(l):
    if item == -1:
        if i == 0 and n > 1:
            ans += '1'
        else:
            ans += '0'
    else:
        ans += str(item)
print(ans if flag else -1)
