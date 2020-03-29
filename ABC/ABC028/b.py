s=input()
ans = []
st=''
for item in ['A','B','C','D','E','F']:
    ans.append(s.count(item))

for i in range(len(ans)):
    if i != 0:
        st += ' '
    st += str(ans[i])
print(st)