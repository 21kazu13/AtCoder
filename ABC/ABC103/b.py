s = input()
t = input()
n = len(s)

for i in range(n):
    if t == s:
        print('Yes')
        exit()
    else:
        s = s[-1] + s[:-1:]
    
print('No')