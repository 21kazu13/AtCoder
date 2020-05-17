s = input()
t = input()
tmp = s*2
num = len(s)
for i in range(num):
    st = tmp[i:i+num]
    if st == t:
        print('Yes')
        exit()
print('No')