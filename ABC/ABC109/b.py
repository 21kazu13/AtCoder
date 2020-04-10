def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
wl = [input()]
rule = True
for i in range(1,n):
    s = input()
    if s in wl or s[0] != wl[-1][-1]:
        rule = False
    wl.append(s)

if rule:
    print('Yes')
else:
    print('No')