n = int(input())
p = 1
for i in range(1,n+1):
    p *= i
    p = p%1000000007
print(p)