s = input()
s_rev = s[::-1]

for x,y in zip(s,s_rev):
    if x != y and x != '*' and y != '*':
        print('NO')
        exit()
print('YES')