s = input()
a = int(s[0])
b = int(s[1])
c = int(s[2])
d = int(s[3])

for i in range(8):
    output = []
    for j in range(3):
        if ((i >> j) & 1) == 1:
            output.append('+')
        else:
            output.append('-')
    ans = 0
    ansstr = ''
    for i in range(4):
        if i == 0:
            ans += int(s[i])
            ansstr += s[i]
        elif output[i-1] == '+':
            ans += int(s[i])
            ansstr += output[i-1]
            ansstr += s[i]
        else:
            ans -= int(s[i])
            ansstr += output[i-1]
            ansstr += s[i]
    if ans == 7:
        print(ansstr+'=7')
        exit()
