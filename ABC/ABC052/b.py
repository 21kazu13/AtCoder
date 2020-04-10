n = int(input())
n = 0
ans = 0
s = input()

for i in s:
    if i == 'D':
        n -= 1
    else:
        n += 1
    ans = max(n,ans)
print(ans)