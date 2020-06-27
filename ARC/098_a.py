def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

n = ii()
s = input()
left = s[1:].count('W')

dp = [[0,left]]
ans = n-1-left
last = s[0]
for i in s[1:]:
    ri,le = dp[-1]
    if i == 'W':
        le -= 1
    if last == 'E':
        ri += 1
    dp.append([ri,le])
    last = i
    ans = min(ans,n-1-ri-le)
print(ans)