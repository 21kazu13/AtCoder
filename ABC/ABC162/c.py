import math
k = int(input())
ans = 0
if k < 3:
    for i in range(1,k+1):
        for j in range(1,k+1):
            for n in range(1,k+1):
                ans += math.gcd(i,math.gcd(j,n))
else: 
    #i*j
    for n in range(1,k+1):
        for i in range(1,k+1):
            ans += math.gcd(n,i)
            for j in range(i+1,k+1):            
                ans += 2*(math.gcd(math.gcd(i,j),n))

print(ans)

'''
PyPy3だと普通の3重ループで通る
import math
k = int(input())
ans = 0
for i in range(1,k+1):
    for j in range(1,k+1):
        for n in range(1,k+1):
            ans += math.gcd(i,math.gcd(j,n))
print(ans)
'''
