import collections

d = {}
n = int(input())
ans = 0
for i in range(n):
    st = list(input())
    st.sort()
    s = ''.join(st)
    m = d.get(s,False)
    if m:
        ans += m
        d[s] = m+1
    else:
        d[s] = 1 

print(ans)