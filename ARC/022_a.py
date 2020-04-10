s = input().upper()

ii = s.find('I')
if ii == -1:
    print('NO')
    exit()
ci = s.find('C',ii+1)
if ci == -1:
    print('NO')
    exit()
ti = s.find('T',ci+1)
if ti == -1:
    print('NO')
else:
    print('YES')
