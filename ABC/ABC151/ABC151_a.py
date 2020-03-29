alpha = list('abcdefghijklmnopqrstuvwxyz')
c = input()

for i in range(26):
    if alpha[i] == c:
        print(alpha[i+1])
        exit()