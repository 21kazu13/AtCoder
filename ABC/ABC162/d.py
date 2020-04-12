def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
s = list(input())
baf = s.count('B')
raf = s.count('R')
gaf = s.count('G')
bbf = 0
rbf = 0
gbf = 0
ans = 0
for i,item in enumerate(s):
    if item == 'B':
        baf -= 1
        bbf += 1
        ans += rbf*gaf
        ans += raf*gbf
    elif item == 'R':
        raf -= 1
        rbf += 1
        ans += bbf*gaf
        ans += baf*gbf
    else:
        gaf -= 1
        gbf += 1
        ans += rbf*baf
        ans += raf*bbf
cnt = 0
for i in range(n):
    num = min(i,n-1-i)
    for j in range(1,num+1):
        if s[i-j] != s[i+j] and s[i-j] != s[i] and s[i+j] != s[i]:
            cnt += 1
print(ans-cnt)
