s = input()
s = list(s)
ans = []
for item in s:
    if item == '0' or item == '1':
        ans.append(item)
    else:
        if len(ans) !=0:
            ans.pop(-1)
print(''.join(ans))