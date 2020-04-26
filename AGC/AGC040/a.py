s = input()

ans = 0
cnt = 0
for i in s:
    if i == '>':
        cnt += 1
    else:
        ans += (cnt**2 - cnt)//2
        cnt = 0
'''
0<3>2>1>0<1<2>0<1<2<3<4<5>2>1>0<1
< : 9
> : 7
'''