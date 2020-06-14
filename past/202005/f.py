def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

from collections import Counter

n = ii()
l = [input() for _ in range(n)]
ans = ''
cent = ''
for i in range(n//2):
    al = Counter(l[i])
    comp = set(l[n-1-i])
    flag = False
    for item in al.keys():
        if item in comp:
            flag = item
            break
    if flag:
        ans += item
    else:
        print(-1)
        exit()
if n%2 == 1:
    cent = l[n//2][0]

print(ans+cent+ans[::-1])