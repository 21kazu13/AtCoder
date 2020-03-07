N = int(input())
A = list(map(int, input().split()))
ans = 0

while(1):
    flag = 0
    for i in A:
        if i%2 == 1:
            flag = flag+1
    if flag==0:
        ans = ans+1
        A = [int(i/2) for i in A]
    else:
        break
print(ans)
