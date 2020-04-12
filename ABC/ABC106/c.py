import re
s = input()
k = int(input())

if s[0] != '1':
    print(s[0])
    exit()
else:
    pos = re.search(r'1+',s).end()
    if k <= pos:
        print(1)
    else:
        print(s[pos])