s = input()

sn = not ('N' in s)^('S' in s)
ew = not ('E' in s)^('W' in s)

if sn and ew:
    print('Yes')
else:
    print('No')