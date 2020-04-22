s = input()
s = s[:-1]
while True:
    num = len(s)
#    print(s,s[:num//2],s[num//2:])
    if num%2 == 0 and s[:num//2] == s[num//2:]:
        print(len(s))
        exit()
    else:
        s = s[:-1]