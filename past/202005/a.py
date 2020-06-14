def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

s = input()
t = input()

s_up = s.upper()
t_up = t.upper()

if s == t:
    print('same')
elif s_up == t_up:
    print('case-insensitive')
else:
    print('different')