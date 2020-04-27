s = input()
di = len(s)
s = int(s)
l = [0]*2019

for i in range(di):
    num = s%10**(di-i)#sが長すぎてダメみたい
    l[num%2019] += 1
#    print(l[0])
ans = l[0]
for i in l:
    if i > 1:
        ans += (i*i-i)//2
print(ans)