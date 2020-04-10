s = input()
t = input()
le = len(s)
count = 0
if le != len(t):
    print(-1)
else:
    for i in range(le):
        if s == t:
            print(count)
            exit()
        else:
            s = s[-1] + s[:le-1]
            count += 1
    print(-1)