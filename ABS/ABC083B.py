n, a, b = map(int, input().split())
ans = 0
for i in range(0,n+1):
    sumofcol = 0
    for j in range(0, len(str(i))):
        sumofcol = sumofcol + int(str(i)[j])
    if a <= sumofcol <= b:
        ans = ans + i
print(ans)