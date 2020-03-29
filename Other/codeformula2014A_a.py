n = int(input())
i = 0
while True:
    i += 1
    ret = i**3
    if ret == n:
        print('YES')
        exit()
    elif ret > n:
        print('NO')
        exit()
    