# n%i == 1となるiを求める->n-1の約数を求める
n = int(input())
if n == 2:
    print(1)
    exit()
ans = []
divisors = []
for i in range(2,int(n**0.5)+1):
    #n-1の約数は全部
    if (n-1) % i == 0:
        ans.append(i)
        if i != (n-1) // i:
            ans.append((n-1)//i)
    #nの約数はやってみる
    if n % i == 0:
        divisors.append(i)
        if i != n // i:
            divisors.append(n//i)
for item in divisors:
    num = n
    while num%item == 0:
        num = num//item
    if num%item == 1:
        ans.append(item)
#print(divisors)
#print(ans)
print(len(ans)+2)#k=n,n-1がはいっていないので+2

'''
import math
n = int(input())
ans = []
divisors = []

for i in range(2,math.ceil(n**0.5)+1):
    num = n
    while num >= i:
        if num%i == 0:
            num //= i
        else:
            num -= i
    print(num)
    if num == 1:
        ans.append(i)
    if n % i == 0:
        divisors.append(i+1)
        if i != n // i:
            divisors.append(n//i+1)

print(ans)
print(divisors)
print(len(ans)+len(divisors))

#[2, 3, 4, 5, 10, 20, 157, 314, 628, 785, 1570, 3140, 3141]
'''