s = list(input())
ans = 0

for i in range(len(s)-1):
    if s[i] == 'B' and s[i+1] == 'W':
        ans += 1
    elif s[i] == 'W' and s[i+1] == 'B':
        ans += 1
print(ans)    