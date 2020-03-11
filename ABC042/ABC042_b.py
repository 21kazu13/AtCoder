n, l = map(int, input().split())
s = [0]*n
for i in range(n):
    s[i] = input()

s.sort()
print(''.join(s))