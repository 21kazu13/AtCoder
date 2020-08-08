def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
s = input()
t = input()
ans = 0
for x,y in zip(s,t):
    if x != y:
        ans += 1
print(ans)