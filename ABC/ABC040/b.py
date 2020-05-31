n = int(input())

ans = int(1e10)
for i in range(1,int(n**0.5)+2):
    other = n//i
    dif = abs(i-other)
    mod = n-i*other
    ans = min(ans,dif+mod)
print(ans)  