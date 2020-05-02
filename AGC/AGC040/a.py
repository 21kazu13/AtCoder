s = input().replace('><','> <').split()
ans = 0
#print(list(s))
for st in s:
    lt = st.count('<')
    gt = len(st) - lt
    if lt > gt:
        gt -= 1
    else:
        lt -= 1
    ans += (lt**2+lt)//2 + (gt**2+gt)//2
print(ans)