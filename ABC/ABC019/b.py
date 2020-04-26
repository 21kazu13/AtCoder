s = input()

ans = ''
cnt = 0
tmp = ''
for i in s:
#    print(i,tmp)
    if i == tmp:
        cnt += 1
    else :
        if cnt != 0:
            ans += (tmp+str(cnt))
        tmp = i
        cnt = 1
#    print(ans)
print(ans+tmp+str(cnt))