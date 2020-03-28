s = input()

if s[0] == s[len(s)-1] and len(s)%2 != 0:
    print('Second')
elif s[0] != s[len(s)-1] and len(s)%2 == 0:
    print('Second')
else:
    print('First')
