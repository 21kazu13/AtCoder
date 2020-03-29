c = 'CODEFESTIVAL2016'
s = input()
ans = 0
for i in range(len(c)):
    if c[i] != s[i]:
        ans += 1
print(ans)