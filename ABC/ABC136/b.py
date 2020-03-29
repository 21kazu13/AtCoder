n = int(input())
digit = len(str(n))

ans = 0
for i in range(1,digit+1):
    if i%2 == 1:
        if i == digit:
            if  i == 1:
                ans += n
            else:
                ans += n-int('9'*(i-1))
        else:
            ans += 9*10**(i-1)
print(ans)
