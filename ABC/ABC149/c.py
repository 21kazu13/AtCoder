x = int(input())
ans = x

while True:
    d = True
    for i in range(2,int(ans**0.5)+1):
        if ans%i == 0:
            d = False
    if d:
        print(ans)
        exit()
    else:
        ans += 1