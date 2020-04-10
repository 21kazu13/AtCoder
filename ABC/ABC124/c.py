s = list(input())
cnt = 0
for i in range(1,len(s)):
#    print(s[i-1],s[i])
    if s[i] == s[i-1]:
        cnt += 1
        if s[i] == '1':
            s[i] = '0'
        else:
            s[i] = '1'
print(cnt)