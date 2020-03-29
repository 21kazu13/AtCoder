s = input()
if 'C' in s:
    n = s.index('C')
    if 'F' in s[n:]:
        print('Yes')
        exit()
print('No')
