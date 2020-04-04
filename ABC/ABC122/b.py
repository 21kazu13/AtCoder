s = list(input())
ans = 0
cnt = 0
for i in s:
    if i in ['A','C','G','T']:
        cnt += 1
    else:
        cnt = 0
    ans = max(cnt,ans)

print(ans)