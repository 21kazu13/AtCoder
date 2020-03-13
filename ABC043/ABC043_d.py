s = list(input())

alpha = [[0 for i in range(2)] for j in range(26)]

def conv(t):
    if t == 'a':
        return 0
    elif t == 'b':
        return 1
    elif t == 'c':
        return 2
    elif t == 'd':
        return 3
    elif t == 'e':
        return 4
    elif t == 'f':
        return 5
    elif t == 'g':
        return 6
    elif t == 'h':
        return 7
    elif t == 'i':
        return 8
    elif t == 'j':
        return 9
    elif t == 'k':
        return 10
    elif t == 'l':
        return 11
    elif t == 'm':
        return 12
    elif t == 'n':
        return 13
    elif t == 'o':
        return 14
    elif t == 'p':
        return 15
    elif t == 'q':
        return 16
    elif t == 'r':
        return 17
    elif t == 's':
        return 18
    elif t == 't':
        return 19
    elif t == 'u':
        return 20
    elif t == 'v':
        return 21
    elif t == 'w':
        return 22
    elif t == 'x':
        return 23
    elif t == 'y':
        return 24
    elif t == 'z':
        return 25
index = 0
for i in s:
#    print(str(index)+i)
    if alpha[conv(i)][0] == 0:
        alpha[conv(i)][0] = 1
        alpha[conv(i)][1] = index
    else:
        alpha[conv(i)][0] += 1
        if index-alpha[conv(i)][1]+1 < 2*alpha[conv(i)][0]:
            print(alpha[conv(i)][1]+1,index+1)
            exit()
        else:
            alpha[conv(i)][0] = 1
            alpha[conv(i)][1] = index
    index += 1
#    print(alpha)

print(-1,-1)