s = list(input())
n = len(s)
ans = 0
for i,item in enumerate(s):
    if item == 'U':
        ans += n-1+i
    else:
        ans += 2*n-i-2
print(ans)