import math
n = int(input())
ans = 0
if n > 104:
    for i in range(105,n+1)[::2]:
        cnt = 0
        for j in range(1,math.ceil(i**0.5)):
            if i%j == 0:
                cnt += 2
            if j**2 == i:
                cnt -= 1
        if cnt == 8:
            ans += 1
print(ans)